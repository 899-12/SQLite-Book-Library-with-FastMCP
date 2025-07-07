# 📚 SQLite Book Library with FastMCP

This project implements a simple **Book Library backend** using:

- 🛠️ **FastMCP**: to expose Python functions as AI-callable tools  
- 🗄️ **SQLite**: to store book data  
- ⚙️ **Uvicorn**: to serve the tools over an HTTP SSE interface

It allows Language Models (LLMs) to interact with your local database through tool calls — ideal for Retrieval-Augmented Generation (RAG), autonomous agents, or database assistants.

---

## 🚀 Features

- 📖 Add new books using SQL
- 🔍 Query books with custom `SELECT` queries
- 🧠 Designed to integrate with LLM agents (e.g., via LlamaIndex)
- 🧰 Easily extendable: add `update_book()` or `delete_book()` as needed

---

## 🔧 Tech Stack

| Component     | Description                                       |
|---------------|---------------------------------------------------|
| `FastMCP`     | Lightweight implementation of the MCP standard    |
| `SQLite`      | File-based local database (`library.db`)          |
| `Uvicorn`     | ASGI server to host the tool interface            |
| `LlamaIndex`  | Agent framework to interact with MCP tool servers |

---

## ⚙️ What is MCP?

**MCP (Model Context Protocol)** is an open standard designed to help applications connect large language models (LLMs) to external tools and data.  
Think of MCP like a **USB-C port for LLMs**: it standardizes the way models call functions and access data sources.

### Why use MCP?

- 🔌 **Tool interoperability** – Easily expose Python functions as callable APIs
- 🧠 **Plug-and-play LLM agents** – LLMs can auto-discover and use tools
- 🔐 **Vendor-agnostic** – Use with OpenAI, Anthropic, Hugging Face, or local models
- 🏗️ **Workflow-friendly** – Ideal for building modular AI agents and pipelines

---

## 🛠️ Local MCP Setup

### `server.py` – Your tool server
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP('sqlite-book-library')  # Register your toolset

To start the server:
```
uv run server.py --server_type=sse
```

## 🤖 How LLM Agents Use This
Agents connect to your MCP server and call tools directly using natural language instructions.

Example client setup:
```
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

mcp_client = BasicMCPClient("http://127.0.0.1:8000/sse")
mcp_tools = McpToolSpec(client=mcp_client)
```
This client will auto-discover tools like add_book, get_books, and more.

✨ Example instruction to LLM:
“Add a book titled The Alchemist by Paulo Coelho, published in 1988, genre Fiction.”

The LLM will convert this into a SQL INSERT and call the add_book() tool.

