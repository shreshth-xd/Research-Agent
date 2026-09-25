# Research Agent

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agents-1C3C78?style=for-the-badge)](https://www.langchain.com/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-Gemma_4-8A2BE2?style=for-the-badge)](https://openrouter.ai/)
[![DeepAgents](https://img.shields.io/badge/DeepAgents-Experimental-00C2A8?style=for-the-badge)](https://github.com/langchain-ai/deepagents)
[![dotenv](https://img.shields.io/badge/dotenv-Environment-5B5BD6?style=for-the-badge)](https://pypi.org/project/python-dotenv/)

</div>

A research-oriented agent built to fetch public text from the web, reason over it, and answer evidence-based questions using tool calling and conversational memory.

## Overview

This project is a lightweight experimentation ground for a document research assistant. Instead of hardcoding a single task, it gives an LLM a real tool for retrieving document content and a memory layer so it can keep track of the workflow while answering grounded questions about a source text.

The current implementation is focused on literary and reference-style research tasks: it downloads a text file from a URL, reads the raw content, and uses the model to answer questions such as:

- how many lines contain a keyword
- where a term first appears
- what the text is about
- whether the answer can be verified from the source text

This makes the project useful as a prototype for research assistants, document QA pipelines, and grounded text analysis workflows.

## Scope and Purpose

The agent is intentionally narrow in purpose but extensible in design:

- fetch document text from a URL
- provide the retrieved content to a language model
- use a system prompt to constrain behavior and encourage evidence-based answers
- run a standard LangChain agent and a DeepAgent-style variant for comparison
- maintain state using an in-memory checkpointer for session continuity

In short, this repository is not a general-purpose app with a large UI or production backend. It is a focused AI agent project for reading source material and answering research-like questions grounded in that material.

## Architecture

The project is organized around a small set of core files:

- `agent.py` — creates the main agent and the deeper research-oriented agent
- `model.py` — initializes the LLM through OpenRouter
- `tools.py` — contains the `fetch_text_from_url` tool that retrieves web content
- `prompts.py` — central prompt configuration for the agent
- `state.py` — defines the in-memory conversation checkpoint
- `requirements.txt` — Python dependencies

## How It Works

1. The model is configured in `model.py` using a hosted OpenRouter endpoint.
2. A tool in `tools.py` fetches raw text from a URL and decodes it safely.
3. `agent.py` wires the model, tool, prompt, and state together to create an agent.
4. The agent receives a research prompt, fetches the relevant text, and answers using the retrieved document rather than guessing.
5. A second `deep_agent` is created to experiment with a more advanced, deeper reasoning workflow.

## Example Use Case

The repository includes a concrete example based on a Project Gutenberg text: it fetches the full text of The Great Gatsby and asks the agent to determine:

- how many lines contain the substring `Gatsby`
- the first line number containing `Daisy`
- a neutral synopsis of the text

This pattern is representative of the broader use case: give the agent a public document, ask grounded questions, and verify the answers against the source text.

## Tech Stack

- Python
- LangChain
- DeepAgents
- OpenRouter
- Gemini-style hosted model access
- python-dotenv
- InMemorySaver

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENROUTER_API_KEY="your_api_key_here"
python agent.py
```

## Environment Setup

This project expects an API key for OpenRouter in the environment:

```bash
export OPENROUTER_API_KEY="your_openrouter_key"
```

The model configuration in `model.py` uses the OpenRouter-compatible endpoint and loads the key from the environment.

## Current Behavior

This repository is a prototype and is best understood as a research assistant skeleton:

- it is designed for URL-based text retrieval
- it favors evidence-grounded responses
- it uses in-memory persistence, not a durable database
- it is built for experimentation and extension, not for production deployment

## Notes

- The agent is strongly dependent on the model and prompt design for quality.
- Current memory is in-memory only, so state resets when the process ends.
- The tool layer is intentionally minimal and can be extended with web search, document parsing, or structured data extraction.

## Future Extensions

Possible next steps for this project include:

- support for multiple URLs and document types
- parsing PDFs and HTML pages
- storing research memory across sessions
- adding task decomposition and planning steps
- web search integration for broader research workflows

---

Built as a compact research-agent prototype for grounded text analysis and document-based Q&A.
