from importss import *
from Rag_pipeline import rag 
from task_managing import create_calendar_event, list_upcoming_events, cancel_calendar_event
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()


env = os.getenv("tavily_API_KEY")
tav =TavilyClient(env)


# search = GoogleSerperAPIWrapper()


# results = DDGS().text("python Programming", max_results=5)
# print(results)
@tool
def search_agent(query):
    """
    only use this tool when you are not aware of the question , if u are not aware of the question and it is not inside your knowlwdge base you can use this tool , but not always use this tool for every information
    search the web for accurate and up-to-date information.
    Use this tool when you need real-time or external knowledge

    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query,max_results=5)

            formatted = []


            for r in results:
                formatted.append(
                f"""Title : {r['title']},
URL : {r["href"]},
snippet : {r['body']}""")
                
            return "\n\n".join(formatted)


    except Exception as e:
        return f" error occured {e}"






# @tool
# def search_agent(query):
    

    # try:
    #     response = tav.search(
    #         query=query,
    #         search_depth="basic"
    #     )
    #     print(response)
    #     if results in response:
    #         results=[]
    #         for r in response["results"][:2]:
    #             content = r.get("content","")
    #             results.append(content[:400])

    #         return "\n".join(results)
    #     else:
    #         return "no results found for the given query"
        
    # except Exception as e:
    #     return f"error occured during the search{str(e)}"
    



@tool 
def open_apps(apps_name : str):

    """ It will open the app that user want him to open 

    Args:
    apps : Its a dictionary that access the key
    apps_name : user input , the app that he wanted to open
    
    
    """
    try:
        apps = {

        # editors / IDEs
        "vscode": "code",
        "visual studio code": "code",
        "notepad": "notepad",
        "notepad++": "notepad++",
        "sublime": "subl",
        "pycharm": "pycharm64",
        "intellij": "idea64",
        "android studio": "studio64",
        "vs code": "code",
        "visual studio" : "code",
        "browser" : "brave",


        # browsers
        "chrome": "chrome",
        "google chrome": "chrome",
        "edge": "msedge",
        "microsoft edge": "msedge",
        "firefox": "firefox",
        "brave": "brave",

        # system tools
        "calculator": "calc",
        "paint": "mspaint",
        "command prompt": "cmd",
        "cmd": "cmd",
        "powershell": "powershell",
        "task manager": "taskmgr",
        "registry editor": "regedit",

        # file system
        "file explorer": "explorer",
        "explorer": "explorer",
        "file" : "explorer",

        # media
        "media player": "wmplayer",
        "windows media player": "wmplayer",
        "vlc": "vlc",

        # office
        "word": "winword",
        "excel": "excel",
        "powerpoint": "powerpnt",
        "outlook": "outlook",
        "ms word": "winword",
        "ms excel":"excel",

        # communication
        "whatsapp": "whatsapp",
        "telegram": "telegram",
        "discord": "discord",
        "zoom": "zoom",

        # dev tools
        "docker": "docker",
        "git bash": "git-bash",
        "github desktop": "github",
        "postman": "postman",

        # utilities
        "control panel": "control",
        "settings": "ms-settings:",
        "device manager": "devmgmt.msc",
        "disk management": "diskmgmt.msc",

        # screenshots
        "snipping tool": "snippingtool",

        # windows security
        "windows security": "windowsdefender:"
            }
        

        apps_name = apps_name.lower()
        if apps_name in apps:
            os.system(f"start {apps[apps_name]}")
            return f"{apps_name} opened"
       
        else:
            return "app not avalaible "
    except Exception as e:
        return f"error occured {e}"
    

try:
    @tool
    def rag_tool(query:str):
        """This tool will help the agent to retrieve context from document"""
        response = rag.vector_db.similarity_search(query=query,k=4)
        context = ""

        for doc in response:
            context = doc.page_content + "\n\n"
        return context 




except Exception as e:
    print(f"error occured at {e}")



try:
    agent = create_agent(
        model = llm,
        tools= [search_agent,open_apps,rag_tool,create_calendar_event, list_upcoming_events, cancel_calendar_event],
        checkpointer=memory,
        system_prompt= """You are a desktop AI assistant with access to tools.

You have exactly 3 tools:
1. open_apps — use when user wants to open any application
2. search_agent — use when user needs current, recent, or uncertain information
3. rag_tool — use when user asks about an uploaded document or PDF

DECISION FLOW — follow this exact order:

STEP 1: Does user want to open an app?
→ YES: call open_apps
→ NO: go to step 2

STEP 2: Does the question mention a document, PDF, file, author, 
        university, organization from a document, or any context 
        that would only be in an uploaded file?
→ YES: call rag_tool immediately, do not ask user for context
→ NO: go to step 3

STEP 3: Could this answer have changed in the last 2 years?
→ YES (current events, live scores, recent news, weather): call search_agent
→ NO (historical facts, science, math, famous people's basic bio): answer directly

SELF-ANSWER examples (never use tools for these):
- "Who was the first PM of India?"
- "What is photosynthesis?"
- "Who won ICC T20 WC 2024?" (past, settled event)
- "What is 15% of 200?"
- Basic definitions, established science, math

search_agent examples:
- "Who won ICC T20 WC 2026?" (recent/current)
- "What is the weather today?"
- "Latest news about AI"
- Anything you are not confident about

rag_tool examples:
- "Who is the author of this document?"
- "What is the name of the university in the PDF?"
- "What does the document say about X?"
- Any question where context must come from uploaded file

STRICT RULES:
- Never call a tool for something you already know
- When using search_agent: only reply with what search_agent returns, no extra lines
- Only reply in ENGLISH
- Never print your decision process in terminal
""")
except Exception as e:
    print(f"error occured at {e}")







    







# def open_apps(command):
#     command = command.lower()

#     if any(word in command for word in ["vscode","vs","code","visual studio","studio"]):
#         os.system("code")

#     elif "calculator" in command:
#         os.system("calc")

#     elif "spotify" in command:
#         os.system("spotify")

#     elif "brave" in command:
#         os.system("start brave")

#     elif "" in command:
#         os.system("")
    
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
    
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
    
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
    
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
#     elif "" in command:
#         os.system("")
        


#     else:
#         print("not found")

# cmd = input("which app u want to open: ")
# open_apps(cmd)