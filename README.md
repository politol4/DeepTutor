# DeepTutor Evaluation System

DeepTutor is an intelligent tutoring system built around multi-agent collaboration and RAG. This repository is the paper evaluation variant, focused on four core modules: **Question Generation**, **Question Solving**, **RAG**, and **Memory / Personalization**.

## System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    CLI / Evaluation Scripts                │
├──────────────┬──────────────┬───────────────┬──────────────┤
│  Question    │    Solve     │    Memory     │  Benchmark   │
│  Generation  │    Agent     │ Personalize   │ + SimuTool   │
├──────────────┴──────────────┴───────────────┴──────────────┤
│                       Shared Tool Layer                    │
│          RAG Tool · Web Search · Code Executor            │
├─────────────────────────────────────────────────────────────┤
│                      Foundation Services                   │
│     LLM Service · Embedding · RAG Pipeline · Knowledge    │
└─────────────────────────────────────────────────────────────┘
```

### Core Modules

- **Question Module** (`src/agents/question/`): Uses a dual-loop architecture with an idea loop and a generation loop. Supports both topic-driven and exam-mimic question generation.
- **Solve Module** (`src/agents/solve/`): Uses a three-stage `Plan -> ReAct -> Write` pipeline with multi-step planning, tool use, and citation support.
- **RAG Service** (`src/services/rag/`): Provides a unified RAG pipeline with support for backends such as LlamaIndex, LightRAG, and RAG-Anything.
- **Memory System** (`src/personalization/`): Uses a Trace Forest-based personalization framework with reflection, summary, and weakness-analysis agents.

## Installation

### Requirements

- Python 3.10 or later
- `pip`

### Setup

```bash
git clone <repo-url>
cd DeepTutor

python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Configuration

Copy the environment template and fill in the required values:

```bash
cp .env.example .env
```

Required settings include:

| Key | Description |
|------|-------------|
| `LLM_BINDING` | LLM provider binding such as `openai`, `anthropic`, or `deepseek` |
| `LLM_MODEL` | Model name such as `gpt-4o` |
| `LLM_API_KEY` | API key for the LLM provider |
| `LLM_HOST` | API endpoint |
| `EMBEDDING_BINDING` | Embedding provider binding |
| `EMBEDDING_MODEL` | Embedding model name |
| `EMBEDDING_API_KEY` | API key for the embedding provider |
| `EMBEDDING_HOST` | Embedding endpoint |
| `EMBEDDING_DIMENSION` | Embedding vector dimension |

Optional settings such as `SEARCH_PROVIDER` and `SEARCH_API_KEY` are documented in `.env.example`.

## CLI Usage

### Interactive Launcher

```bash
python start.py
```

This launches an interactive menu for the solver and question-generation modules.

### Solve CLI

```bash
# Solve one question
python -m src.agents.solve.cli "What is linear convolution?" --kb Calculus

# Detailed iterative answer mode
python -m src.agents.solve.cli "What is linear convolution?" --detailed

# Interactive mode
python -m src.agents.solve.cli -i --language zh
```

### Question CLI

```bash
python src/agents/question/cli.py
```

Supported modes:

- **Topic mode**: Generate questions from a topic or concept.
- **Mimic mode**: Generate questions by mimicking an input exam PDF.

### Memory System

The memory system is initialized automatically when `start.py` launches. Learning events from solving and question generation are captured by the EventBus and processed by three memory agents in parallel, which then update user memory documents.

## Evaluation Framework

### Simulator Tools (`benchmark/simulation/`)

The student simulator uses isolated workspace tools:

- `solve_question()`: Runs the full `Plan -> ReAct -> Write` solve pipeline
- `generate_questions()`: Generates multiple-choice questions while hiding answers from the student
- `submit_answers()`: Submits answers, grades them automatically, and triggers memory updates

See `benchmark/simulation/USE.md` for more details.

### Benchmark Framework (`benchmark/`)

The benchmark framework includes:

- **Data generation** (`benchmark/data_generation/`): Generates evaluation data from knowledge bases, student profiles, knowledge gaps, and tasks
- **Conversation simulation** (`benchmark/simulation/`): Runs multi-turn interactions between LLM-driven students and tutors
- **Evaluation** (`benchmark/evaluation/`): Uses LLM-as-Judge scoring at both turn and dialogue levels

```bash
python -m benchmark.evaluation.run <transcript_path>
```

## Repository Structure

```text
DeepTutor/
├── benchmark/                 # Evaluation framework
├── config/
│   ├── agents.yaml            # Agent temperature and max_tokens settings
│   ├── main.yaml              # Main configuration
│   └── memory.yaml            # Memory-system configuration
├── data/
│   ├── knowledge_bases/       # Knowledge base storage
│   └── user/                  # User outputs and memory data
├── start.py                   # CLI launcher
├── src/
│   ├── agents/
│   │   ├── question/          # Question-generation pipeline
│   │   └── solve/             # Solve pipeline
│   ├── config/                # Constants and default values
│   ├── core/                  # EventBus and base errors
│   ├── knowledge/             # Knowledge-base management
│   ├── logging/               # Unified logging system
│   ├── personalization/       # Memory and personalization logic
│   ├── services/              # Configuration, LLM, RAG, search, setup, etc.
│   ├── tools/                 # Code execution, RAG, web search, question tools
│   └── utils/                 # Shared utilities
├── tests/                     # Unit tests
├── .env.example               # Environment template
├── pyproject.toml             # Python project configuration
└── requirements.txt           # Python dependencies
```

## Configuration Files

| File | Description |
|------|-------------|
| `config/agents.yaml` | Temperature and max token settings for each module |
| `config/main.yaml` | Paths, tools, solve/question settings, and shared system configuration |
| `config/memory.yaml` | Memory-system model and runtime settings |
| `.env` | Environment variables for LLM and embedding credentials |

## License

AGPL-3.0
