# llama4-maverick-demo

This repository demonstrates how to use the LLaMA 4 Maverick model (via Fireworks AI) with a 1M-token context window to analyze the entire PyTorch codebase in a single prompt.

## Project Overview

Large Language Models (LLMs) are revolutionizing code analysis, documentation, and understanding. With the advent of models like LLaMA 4 Maverick, which supports a 1 million token context window, it's now possible to query and analyze entire codebases in a single shot. This project leverages the Fireworks AI API to feed the entire PyTorch codebase into LLaMA 4 Maverick, enabling deep, context-rich queries and insights.

## Features
- Clones the PyTorch repository
- Reads and concatenates all Python files
- Tokenizes and trims the corpus to the last 1,000,000 tokens
- Sends the prompt to LLaMA 4 Maverick via the Fireworks API
- Prints the model's response

## Step-by-Step Usage

1. **Install dependencies:**
   ```bash
   pip install gitpython fireworks-ai tiktoken
   ```
2. **Set your Fireworks API key** in the script.
3. **Run the script** to analyze the PyTorch codebase with LLaMA 4 Maverick.

## How It Works

### 1. Setup and Configuration
```python
API_KEY    = "<Fireworks API Key>"
MODEL_NAME = "accounts/fireworks/models/llama4-maverick-instruct-basic"
client = Fireworks(api_key=API_KEY)
```

### 2. Clone the PyTorch Repository
```python
REPO_URL = "https://github.com/pytorch/pytorch.git"
LOCAL_PATH = "pytorch"
if not os.path.isdir(LOCAL_PATH):
    Repo.clone_from(REPO_URL, LOCAL_PATH)
```

### 3. Read and Concatenate Python Files
```python
corpus = []
for root, _, files in os.walk(LOCAL_PATH):
    for name in files:
        if name.endswith(".py"):
            with open(os.path.join(root, name), "r", encoding="utf-8", errors="ignore") as f:
                corpus.append(f.read())
big_text = "\n".join(corpus)
```

### 4. Tokenize and Trim
```python
enc = tiktoken.encoding_for_model(MODEL_NAME)
all_tokens = enc.encode(big_text)
MAX_CTX = 1_000_000
trimmed = all_tokens[-MAX_CTX:] if len(all_tokens) > MAX_CTX else all_tokens
prompt_text = enc.decode(trimmed)
```

### 5. Query the Model
```python
response = client.chat.completions.create(
    model=MODEL_NAME,
    max_tokens=16384,
    temperature=0.2,
    top_p=1,
    top_k=40,
    presence_penalty=0.0,
    frequency_penalty=0.0,
    prompt_truncate_len=MAX_CTX,
)
```

### 6. Display the Model's Response
```python
print(response.choices[0].message.content)
```

## Why is This Powerful?
- **Massive Context Window:** Analyze entire codebases without chunking or losing context.
- **Flexible Queries:** Ask for summaries, call traces, or cross-module insights.
- **Automation:** The script can be adapted for any large codebase, not just PyTorch.

---

*This project showcases the power of large-context LLMs for holistic codebase analysis.*