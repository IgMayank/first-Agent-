from dotenv import load_dotenv
load_dotenv()

import httpx
import os
from datetime import datetime
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain.agents import create_agent
# from openai import OpenAI
from langchain_openai import ChatOpenAI

CAL_API_KEY = os.getenv("CAL_API_KEY")
EVENT_TYPE_ID = 5182102
YOUR_NAME = "Mayank"
YOUR_EMAIL = "mkdogra1981@gmail.com"

HEADERS = {
    "Authorization": f"Bearer {CAL_API_KEY}",
    "cal-api-version": "2024-09-13",
    "content-type": "application/json"
}

BASE = "https://api.cal.com/v2"


@tool
def create_calendar_event(title: str, start_time: str, duration_minutes: int = 30) -> str:
    """
    Create an event on the calendar. start_time must be YYYY-MM-DD or full ISO 8601.
    Always use the current year when no year is specified.
    """
    if len(start_time) == 10:
        current_year = datetime.now().year
        start_time = f"{current_year}-{start_time[5:]}T11:00:00+05:30"
    else:
        # clamp time to working hours 9AM-5PM IST
        dt = datetime.fromisoformat(start_time.replace("Z", "+05:30"))
        if dt.hour < 9 or dt.hour >= 17:
            dt = dt.replace(hour=11, minute=0, second=0)
        start_time = dt.strftime("%Y-%m-%dT%H:%M:%S+05:30")

    # print(f"[DEBUG] Booking with start_time: {start_time}")

    res = httpx.post(
        f"{BASE}/bookings",
        json={
            "eventTypeId": int(EVENT_TYPE_ID),
            "start": start_time,
            "timeZone": "Asia/Kolkata",
            "language": "en",
            "metadata": {},
            "responses": {
                "name": YOUR_NAME,
                "email": YOUR_EMAIL
            }
        },
        headers=HEADERS,
        timeout=30
    )
    data = res.json()
    # print(f"[DEBUG] STATUS: {res.status_code}, RESPONSE: {data}")
    if data.get("status") == "success":
        uid = data["data"]["uid"]
        return f"Event created! UID: {uid}. Check your Google Calendar."
    return f"Failed: {data.get('error', {}).get('message', 'Unknown error')}"


@tool
def list_upcoming_events() -> str:
    """List all upcoming calendar events/bookings."""
    res = httpx.get(f"{BASE}/bookings?status=upcoming", headers=HEADERS, timeout=30)
    data = res.json()
    if data.get("status") != "success":
        return f"Error: {data}"
    
    bookings = data["data"]
    # print(type(bookings), bookings) 
    if isinstance(bookings, dict):
        bookings = bookings.get("bookings", [])  
    
    if not bookings:
        return "No upcoming events found."
    
    results = []
    for b in bookings:
        results.append(f"- [{b['uid']}] {b.get('title', 'Event')} at {b['startTime']}")  
    return "\n".join(results)


@tool
def cancel_calendar_event(booking_uid: str, reason: str = "cancelled by agent") -> str:
    """Cancel a calendar event by its booking UID. Use list_upcoming_events first to get the UID."""
    res = httpx.post(
        f"{BASE}/bookings/{booking_uid}/cancel",
        json={"cancellationReason": reason},
        headers=HEADERS,
        timeout=30
    )
    data = res.json()
    if data.get("status") == "success":
        return f"Event {booking_uid} cancelled."
    return f"Failed to cancel: {data.get('error', {}).get('message', 'Unknown error')}"


# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     api_key=os.getenv("GROQ_API_KEY"),
# )
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="qwen/qwen-2.5-7b-instruct",
    streaming=True
)

SYSTEM_PROMPT = f"""You are a personal calendar assistant for Mayank.
Today's date is {datetime.now().strftime("%Y-%m-%d")}. Always use this year when resolving dates.

You have 3 tools:
1. create_calendar_event — create a new event
2. list_upcoming_events — show upcoming events
3. cancel_calendar_event — cancel an event by UID

RULES:
- If user wants to create/schedule → call create_calendar_event
- If user wants to view/check → call list_upcoming_events  
- If user wants to cancel/delete → call cancel_calendar_event
- If time is missing → default to 10:00 AM
- If date is relative (tomorrow, next Monday) → convert to exact YYYY-MM-DD using today's date
- DO NOT retry if a tool fails — report the error immediately
- Keep responses short and natural
"""

agent = create_agent(
    model=llm,
    tools=[create_calendar_event, list_upcoming_events, cancel_calendar_event],
    system_prompt=SYSTEM_PROMPT
)

query = input("Ask anything: ")
while query:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        config={"recursion_limit": 10}
    )
    print(result["messages"][-1].content)
    query = input("Ask anything: ")