# 📚 SQLite Book Library with FastMCP

This project implements a simple **Book Library backend** using:

- 🛠️ **FastMCP**: to expose Python functions as AI-callable tools  
- 🗄️ **SQLite**: to store book data  
- ⚙️ **Uvicorn**: to serve the tools over an HTTP SSE interface

It enables Language Models (LLMs) to interact with your database through structured tool calls — perfect for Retrieval-Augmented Generation (RAG), autonomous agents, or LLM-based assistants.

---

## 🚀 Features

- 📖 Add new books using SQL
- 🔍 Query books with custom `SELECT` queries
- 🧠 Designed to work with LLM agents (e.g., via LlamaIndex)
- 🧰 Easily extendable: add tools to delete or update entries

---

## 🔧 Tech Stack

| Component  | Description |
|------------|-------------|
| `FastMCP`  | Exposes Python functions as tools over HTTP |
| `SQLite`   | Local file-based database (`library.db`) |
| `Uvicorn`  | Lightweight ASGI server |
| `LlamaIndex` | For building LLM agent clients |

---

## ⚙️ What is MCP?
MCP (Machine Callable Protocol) is a protocol that enables exposing Python functions as tools that language models (LLMs) can call seamlessly.

With FastMCP, you can:

✅ Define tools using @mcp.tool() decorators

✅ Serve them over HTTP (--server_type=sse)

✅ Let AI agents discover and call them by name

Think of it like: "Turn your Python functions into AI-callable APIs."


## 🔌 Local MCP Setup Flow
server.py — The Backend Server
```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('sqlite-book-library')  # Register the toolset

```
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

