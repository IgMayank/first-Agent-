from importss import *


env = os.getenv("tavily_API_KEY")
tav =TavilyClient(env)


# search = GoogleSerperAPIWrapper()

# results = DDGS().text("python Programming", max_results=5)
# print(results)
@tool
def search_agent(query):
    """
     Search the web for accurate and up-to-date information.
    Use this tool when you need real-time or external knowledge

    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query,max_results=3)

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
    apps : Its a dictnory that access the key
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
    agent = create_agent(
        model = llm,
        tools= [search_agent,open_apps],
        system_prompt= """You are a desktop AI assistant with access to tools.

    You have exactly 2 tools:
    1. open_apps — use when user wants to open any application
    2. search_agent — use when user asks ANYTHING about real world info

    STRICT TOOL CALLING RULES:
    - ANY question about sports, scores, news, weather, current events 
    -> IMMEDIATELY call search_agent. No exceptions.
    - ANY question about opening apps 
    -> IMMEDIATELY call open_apps. No exceptions.
    - IF App did not opened with USER INPUT
    -> RESPONSE WITH COMMAND ERROR AND NOTHING ELSE , simply COMMAND ERROR.


    CRITICAL:
    - Do NOT answer real-world questions from your own memory or training data
    - Do NOT say the event "hasn't happened yet" — search first, then conclude
    - Do NOT make assumptions — if unsure, search
    - You MUST call the tool BEFORE forming any response

    Your job is to call the right tool. Not to reason. Not to predict. Just search.
    """
    )







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