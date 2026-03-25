from importss import *


try:
    while True:
        user_input = input("\n" "Ask Anything: ")
        if user_input.lower() in ["bye","quit","tata","goodbye","byebye","bie","biee"]:
            print("AI: GOOD BYE SIR!")
            break
        else:
            for chunk, metadata in agent.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            stream_mode="messages"
        ):
                if hasattr(chunk, "content") and chunk.content:
                    if not hasattr(chunk, "tool_calls") or not chunk.tool_calls:
                        print(chunk.content, end="", flush=True)
        
        print()  

except Exception as e:
    print(f" Error occured at {e}")