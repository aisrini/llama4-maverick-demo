# llama4-maverick-demo

This repository demonstrates how to use the LLaMA 4 Maverick model (via Fireworks AI) with a 1M-token context window to analyze the entire PyTorch codebase in a single prompt.

## Features
- Clones the PyTorch repository
- Reads and concatenates all Python files
- Tokenizes and trims the corpus to the last 1,000,000 tokens
- Sends the prompt to LLaMA 4 Maverick via the Fireworks API
- Prints the model’s response

## Usage
1. Install dependencies:
   ```bash
   pip install gitpython fireworks-ai tiktoken
   ```
2. Set your Fireworks API key in the script.
3. Run the script to analyze the PyTorch codebase with LLaMA 4 Maverick.

See the script for detailed code and comments.

---

*This project showcases the power of large-context LLMs for holistic codebase analysis.*