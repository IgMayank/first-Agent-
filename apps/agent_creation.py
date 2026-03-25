from importss import *
from Rag_pipeline import rag 
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
    only use this tool when you are not aware of the question , if u are not aware of the question and it is not isnide your knowlwdge base you can use this tool , but not always use this tool for every information
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
        tools= [search_agent,open_apps,rag_tool],
        checkpointer=memory,
        system_prompt= """You are a desktop AI assistant with access to tools.

        You have exactly 3 tools:
        1. open_apps — use when user wants to open any application
        2. search_agent — use when user needs current, recent, or uncertain information
        3. rag_tool - use this tool when user mentions the document or pdf , for eg user asks who is the author of the document/pdf.

        SELF-ANSWER (do NOT call search_agent) when the question is about:
        - Well-known historical facts ("Who was the first PM of India?")
        - Established science, math, or definitions
        - Famous people's basic bio (birth, death, known roles)
        - Events clearly in the past with settled answers

        CALL search_agent when the question is about:
        - Current events, news, live scores, weather
        - Anything that could have changed recently ("Who is the current PM of India?")
        - Upcoming events or predictions
        - Any topic you are not confident about

        CALL open_apps when:
        - User wants to open any application

        CALL rag_tool when:
        -user wanted to know something out of document/pdf

        BASIC RULE:
        -If user ask something that is not related to llm or tools such as open_apps and search_agent , immediately use rag_tool , for eg- if user says who is the author , what is the name of the organixation , what is the name of the univeristy , YOU WILL GET THE CONTEXT FROM DOCUMENT I>R rag_tool , dont ask for context from user simply use rag_tool, immediately call rag_tool, basically if it seems like user is missing a context simply use rag_tool.

        COMMAND ERROR when:
        - App did not open with user input

        DECISION RULE:
        Ask yourself: "Could this answer have changed in the last 2 years?"
        - YES → call search_agent
        - NO  → answer directly from your knowledge
        but not print this staement in the terminal 
        if you are using agent_search only reply with answer that search_agent gives , dont give any extra lines into addition to search_agent answer, 

        STRICT RULE:
        Only and only reply in ENGLISH and no other language.
        )""")
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