<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:141E30,100:243B55&height=220&section=header&text=FirstAgent&fontSize=42&fontColor=ffffff&animation=fadeIn"/>
</p>

<h1 align="center">🤖 FirstAgent</h1>

<p align="center">
  Multi-Tool AI Assistant with Search, RAG, App Automation & Task Handling
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/LLM-Groq-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Framework-LangChain-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Agentic-AI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🔥 Overview

**FirstAgent** is a modular AI assistant that combines multiple tools into one intelligent system.

It can:

- 🔍 Search the web for real-time information  
- 📄 Retrieve answers from custom documents using RAG  
- 🖥️ Open desktop applications automatically  
- 📅 Manage tasks / reminders  
- 🤖 Route user requests to the correct tool dynamically  

---

## 🧠 Why This Project Matters

Most beginner AI projects are just chatbots.

**FirstAgent** goes beyond that by implementing:

- ✅ Tool Calling Logic  
- ✅ Multi-Agent Style Architecture  
- ✅ Real Utility Automation  
- ✅ Retrieval-Augmented Generation  
- ✅ Task Execution Workflows  

👉 Built to simulate real-world AI assistants.

---

## ⚙️ Core Capabilities

### 🔹 Smart Query Routing
Understands user intent and chooses the right tool.

### 🔹 Web Search Tool
Fetches external information when needed.

### 🔹 RAG Pipeline
Uses your own documents (`PDF`, `TXT`, `CSV`) for grounded answers.

### 🔹 Desktop Automation
Launches local applications through commands.

### 🔹 Task Management
Handles scheduled / utility workflows.

---

## 🧠 System Architecture

```text
User Query
   ↓
Main Agent
   ↓
Intent Detection
   ↓
┌───────────────┬───────────────┬──────────────┬──────────────┐
│ Web Search    │ RAG Tool      │ Open Apps    │ Task Manager │
└───────────────┴───────────────┴──────────────┴──────────────┘
   ↓
Tool Output
   ↓
LLM Response
