# DeepTutor

> An intelligent tutoring system powered by large language models, built as a fork of [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

## Overview

DeepTutor is an AI-powered tutoring platform that helps users learn complex topics through interactive conversations, document analysis, and adaptive question generation. It leverages state-of-the-art LLMs to provide personalized learning experiences.

## Features

- 📄 **Document Understanding** — Upload PDFs, papers, or notes and ask questions about them
- 🤖 **Multi-LLM Support** — Works with OpenAI, Anthropic, and local models via Ollama
- 🧠 **Adaptive Learning** — Generates quizzes and exercises based on your knowledge level
- 💬 **Interactive Chat** — Natural conversation interface for exploring topics
- 🔍 **RAG Pipeline** — Retrieval-Augmented Generation for accurate, grounded answers
- 🌐 **Multilingual** — Supports both English and Chinese interfaces

## Quick Start

### Prerequisites

- Python 3.10 or higher
- [Docker](https://docs.docker.com/get-docker/) (optional, for containerized deployment)
- An API key for at least one supported LLM provider

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/DeepTutor.git
   cd DeepTutor
   ```

2. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

### Docker Deployment

```bash
docker compose up --build
```

The application will be available at `http://localhost:7860`.

## Configuration

Copy `.env.example` to `.env` and fill in the required values.

For Chinese users or CN-region deployments, use `.env.example_CN` as your template instead.

Key configuration options:

| Variable | Description | Required |
|---|---|---|
| `OPENAI_API_KEY` | OpenAI API key | Optional |
| `ANTHROPIC_API_KEY` | Anthropic Claude API key | Optional |
| `OLLAMA_BASE_URL` | URL for local Ollama instance | Optional |
| `DEFAULT_LLM_PROVIDER` | Default LLM provider to use | Yes |
| `EMBEDDING_MODEL` | Embedding model for RAG | Yes |
| `VECTOR_DB_PATH` | Path to persist vector database | Yes |

> At least one LLM provider must be configured.

> **Personal note:** I primarily use this with Ollama running locally (`http://localhost:11434`). Set `DEFAULT_LLM_PROVIDER=ollama` and `OLLAMA_BASE_URL=http://localhost:11434` to get started without any API keys.

## Project Structure

```
DeepTutor/
├── app.py                  # Main application entry point
├── pipeline/               # Core RAG and tutoring pipeline
│   ├── ingestion.py        # Document ingestion and chunking
│   ├── retrieval.py        # Vector search and retrieval
│   └── generation.py       # LLM response generation
├── ui/                     #
```
