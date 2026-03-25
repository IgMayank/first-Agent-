from importss import *

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY")
# )

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="qwen/qwen-2.5-7b-instruct",
    streaming=True
)


# z-ai/glm-4.5-air:free





# def llm(query):
#     response = client.chat.completions.create(
#          model="google/gemma-3-4b-it:free",
#          messages=[{"role":"user","content":query}],
#          stream=True
#         )
#     for chunk in response:
#         if not chunk.choices:
#             continue
#         delta = chunk.choices[0].delta
        
#         if delta and delta.content:
#             print(delta.content,end="",flush=True)
#             time.sleep(0.08)





# "qwen/qwen-2.5-7b-instruct",