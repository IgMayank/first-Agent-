<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=240&section=header&text=Mini%20GPT&fontSize=48&fontColor=ffffff&animation=fadeIn"/>
</p>

<h1 align="center">🤖 Mini GPT</h1>

<p align="center">
  Tool-Enabled AI Assistant with Search, Memory, RAG & Real-World Actions
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-Llama%203.3-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLMs-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenRouter-Enabled-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/RAG-HuggingFace-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-red?style=for-the-badge">
</p>

---

# 🚀 What is Mini GPT?

**Mini GPT** is Developed independently in Python by integrating LLM APIs, tools, retrieval pipelines, and automation workflows.  
It combines language models with tools so it can perform useful actions instead of only generating text.

### Current Capabilities

- 🖥️ Open desktop applications  
- 🌐 Search the web using DuckDuckGo  
- 📄 Answer questions from private documents using RAG  
- 📅 Create reminders/events in Google Calendar  
- 🧠 Maintain short-term conversation memory  
- 🤖 Use tools based on user intent  
- ⚡ Supports Groq, OpenRouter, and Ollama backends  

---

# 🔥 Why This Project Stands Out

Most beginner AI projects are simple chatbots.

**Mini GPT** goes further by implementing:

- ✅ Tool calling workflows  
- ✅ Real-world task execution  
- ✅ Search + document retrieval  
- ✅ Memory-aware conversations  
- ✅ Multiple model provider support  
- ✅ Modular project structure  

This project focuses on building a practical assistant system rather than a basic chatbot UI.

---

# 🧠 System Architecture

```text
User Input
   ↓
Mini GPT Core Agent
   ↓
Intent Understanding
   ↓
Select Appropriate Tool
   ↓

┌────────────────────────────┐
│ 🔍 Web Search Tool        │
│ 🖥️ Open Apps Tool        │
│ 📄 RAG Document Tool      │
│ 📅 Calendar Tool          │
│ 🧠 Memory Context         │
└────────────────────────────┘

   ↓
Tool Result Returned
   ↓
LLM Generates Response
   ↓
Final Output to User


--


⚙️ Current Capabilities


🔹 Open Applications

Examples:

Open Chrome
Open VS Code
Open Calculator

🔹 Web Search

Examples:

Search latest AI news
Who won yesterday's IPL match?
Best Python roadmap 2026

🔹 RAG over Documents

Supports:

PDF

Examples:

Summarize mayank.pdf


🔹 Google Calendar Actions

Examples:

Create birthday event on 20 April


🔹 Memory

The assistant remembers recent conversation context for better follow-up responses.

Example:

User: summarize my pdf
User: who is the author?


🛠️ Tech Stack



   Layer           	   Technology
Core Language	  :          Python
LLM APIs	        :      Groq / OpenRouter
Local Models	  :          Ollama
Framework	     :    LangChain / Custom Agents
Search           : 	   DuckDuckGo
RAG	           :   HuggingFace + Vector Store
Automation	     :    Python + OS Commands
Memory	        :   Short-Term Context Memory
