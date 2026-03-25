from importss import *
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore





try:
    class Rag_pipeline():

        def __init__(self):
            self.vector_db = None


        def build_pipeline(self):
            loader = PyPDFLoader("../Data/mayank.pdf")
            docs = loader.load()
            
        
            splitter = RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=500)
            splitted_docs = splitter.split_documents(docs)
           
            embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
            )
            
        
        
            self.vector_db = InMemoryVectorStore.from_documents(
                documents=splitted_docs,
                embedding=embeddings,
            )
            
        
except Exception as e :
    print(f" error occured at {e}")

rag = Rag_pipeline()
rag.build_pipeline()


