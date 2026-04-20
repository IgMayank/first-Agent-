from importss import *

# FOR GREETING PROPERLY
for chunk, metadata in agent.stream(
            {
    "messages": [
        {
            "role": "system",
            "content": "You are a creative AI assistant. Whenever the conversation starts, greet the user in a unique, fun, and slightly personalized way. Never repeat the same greeting,'/n' and also u wanna check the list_upcoming_events tools and tell the user if he have any event today or not , only for the present date and dont list all events ok I REPEAT DONT LIST ALL EVENTS ONLY OF TODAY."
        },
        {
            "role": "user",
            "content": "start"
        }
    ]
},
            config={"configurable":{"thread_id":"abc"}},
            stream_mode="messages"
        ):
                if hasattr(chunk, "content") and chunk.content:
                    # if not hasattr(chunk, "tool_calls") or not chunk.tool_calls:
                    print(chunk.content, end="", flush=True)
        
print()  





# MAIN LOOP FOR TOOL CALLING AND QUESTIONS ANSWER
try:
    while True:
        user_input = input("\n" "Ask Anything: ")
        if user_input.lower() in ["bye","quit","tata","goodbye","byebye","bie","biee"]:
            print("AI: GOOD BYE SIR!")
            break
        else:
            for chunk, metadata in agent.stream(
            {
    "messages": [
        {
            "role": "system",
            "content": "You are a creative AI assistant. Whenever the conversation starts, greet the user in a unique, fun, and slightly personalized way. Never repeat the same greeting."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
},
            config={"configurable":{"thread_id":"abc"}},
            stream_mode="messages"
        ):
                if hasattr(chunk, "content") and chunk.content:
                    if not hasattr(chunk, "tool_calls") or not chunk.tool_calls:
                        print(chunk.content, end="", flush=True)
        
        print()  

except Exception as e:
    print(f" Error occured at {e}")