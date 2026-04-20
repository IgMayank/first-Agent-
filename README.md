<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=240&section=header&text=FirstAgent&fontSize=48&fontColor=ffffff&animation=fadeIn"/>
</p>

<h1 align="center">🤖 FirstAgent</h1>

<p align="center">
  Autonomous AI Assistant with Tools, Memory, Search, RAG & Real-World Actions
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-Llama%203.3-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLMs-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/RAG-HuggingFace-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Memory-Enabled-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Building-red?style=for-the-badge">
</p>

---

# 🚀 What is FirstAgent?

**FirstAgent** is a modular AI assistant built completely from scratch that can:

- 🖥️ Open desktop applications
- 🌐 Search the web using DuckDuckGo
- 📄 Answer questions from custom documents using RAG
- 📅 Create reminders/events in Google Calendar
- 🧠 Remember recent conversation context
- 🤖 Decide which tool to use dynamically
- ⚡ Switch between Groq / OpenRouter / Ollama models

This is not a simple chatbot.

This is an **action-capable AI assistant**.

---

# 🔥 Why This Project Stands Out

Most beginner AI projects are:

- ❌ Just wrappers around ChatGPT APIs
- ❌ No tools
- ❌ No memory
- ❌ No real-world actions
- ❌ No architecture thinking

**FirstAgent solves that by implementing:**

- ✅ Tool Calling Logic
- ✅ Search + Automation + RAG
- ✅ Multi-model support
- ✅ Short-term memory
- ✅ Modular scalable codebase
- ✅ Real utility workflows

---

# 🧠 System Architecture

```text
User Command
   ↓
Main Agent (LLM Brain)
   ↓
Intent Understanding
   ↓
Chooses Best Tool
   ↓

┌────────────────────────────┐
│ 🔍 Web Search Tool        │
│ 🖥️ Open Apps Tool        │
│ 📄 RAG Document Tool      │
│ 📅 Calendar Reminder Tool │
│ 🧠 Memory Context Tool    │
└────────────────────────────┘

   ↓
Tool Executes Task
   ↓
LLM Generates Final Response
   ↓
User Gets Result


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

