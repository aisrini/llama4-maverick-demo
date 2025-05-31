# LLaMA 4 Maverick PyTorch Codebase Analyzer

This project demonstrates how to leverage Fireworks AI's LLaMA 4 Maverick model and its groundbreaking 1-million-token context window to analyze the entire PyTorch codebase in a single inference. The script automates the process of cloning PyTorch, aggregating all Python files, tokenizing the corpus, and querying the LLaMA 4 model for deep codebase insights.

---

## 🚀 Features
- **1M-token context window:** Analyze massive codebases in one go.
- **Automated PyTorch clone:** Always works with the latest codebase.
- **Full Python file aggregation:** Reads and concatenates every `.py` file.
- **Tokenization and context management:** Ensures the prompt fits the model's window.
- **Customizable prompts:** Choose from code structure summaries, call stack traces, or your own queries.
- **Fireworks AI API integration:** Seamless interaction with LLaMA 4 Maverick.

---

## 📂 Project Structure

- `llama4-maverick-code-demo.py` — Main script for codebase analysis
- `README.md` — This documentation
- `pytorch/` — Local clone of the PyTorch repository (auto-generated)

---

## 🛠️ Setup & Installation

### 1. **Clone this repository**
```bash
git clone https://github.com/aisrini/llama4-maverick-demo.git
cd llama4-maverick-demo
```

### 2. **Install dependencies**
You need Python 3.8+ and the following packages:
- `gitpython`
- `fireworks-ai`
- `tiktoken`

Install them via pip:
```bash
pip install gitpython fireworks-ai tiktoken
```

### 3. **Get a Fireworks API Key**
- Sign up at [Fireworks AI](https://fireworks.ai/) and obtain your API key.
- Replace `<Fireworks API Key>` in the script with your actual key.

---

## ⚡ Usage

Run the main script:
```bash
python llama4-maverick-code-demo.py
```

**What happens:**
1. The script clones the PyTorch repo (if not already present).
2. It reads every `.py` file, concatenates them, and tokenizes the result.
3. The last 1,000,000 tokens are used as the prompt for LLaMA 4 Maverick.
4. The model is queried with a customizable prompt (see script for examples).
5. The model's response is printed to the console.

---

## 📝 Customizing the Prompt

In the script, you can choose or modify the prompt for your analysis. Two examples are provided (commented out):
- **Code Structure Summary:**
  - Lists all top-level packages and submodules.
  - Describes high-level data flow (Python → C++ → CUDA).
  - Highlights cross-module helpers.
- **End-to-End Call Stack Trace:**
  - Traces execution from `torch.Tensor.backward()` through all layers.

You can edit or add your own prompts in the `messages` section of the script.

---

## 🔒 Configuration

- **API Key:** Set your Fireworks API key in the `API_KEY` variable.
- **Model:** The script uses `accounts/fireworks/models/llama4-maverick-instruct-basic` by default.
- **Token Limit:** The script trims the prompt to the last 1,000,000 tokens to fit the model's context window.

---

## 🧩 Troubleshooting

- **API Errors:** Ensure your API key is valid and you have access to the LLaMA 4 Maverick model.
- **Dependency Issues:** Double-check that all required Python packages are installed.
- **Large Disk Usage:** The PyTorch repo is large; ensure you have enough disk space.
- **Tokenization Issues:** If you see errors with `tiktoken`, ensure you have the latest version.

---

## 🙋 FAQ

**Q: Can I use this with other codebases?**  
A: Yes! Change the `REPO_URL` and `LOCAL_PATH` variables in the script to analyze any public Git repository.

**Q: Can I use a different model?**  
A: Yes, as long as the model supports large context windows and is available via Fireworks AI.

**Q: How do I change the prompt?**  
A: Edit the `messages` list in the script to ask any question you want about the codebase.

---

## 📜 License

This project is for demonstration and research purposes. See the repository for license details.

---

## ✨ Credits
- [Fireworks AI](https://fireworks.ai/) for the LLaMA 4 Maverick model and API
- [PyTorch](https://github.com/pytorch/pytorch) for the open-source codebase
- [tiktoken](https://github.com/openai/tiktoken) for efficient tokenization