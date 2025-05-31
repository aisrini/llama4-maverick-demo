#!/usr/bin/env python3
"""
Showcase LLaMA 4’s 1M‑token context window by querying the entire
PyTorch codebase in one shot via the Fireworks AI API.
"""

import os
import sys
from git import Repo
from fireworks.client import Fireworks
import tiktoken


# ──────────────
# 1. Setup
# ──────────────

# 1a) Install dependencies:
# ─── Configuration ─────────────────────────────────────────────────────────────
API_KEY    = "<Fireworks API Key>"
MODEL_NAME = "accounts/fireworks/models/llama4-maverick-instruct-basic"
ENDPOINT    = "https://api.fireworks.ai/inference/v1/chat/completions"
HEADERS = {
    "Accept":        "application/json",
    "Content-Type":  "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

client = Fireworks(api_key=API_KEY)


# 1b) Where to clone PyTorch
REPO_URL = "https://github.com/pytorch/pytorch.git"
LOCAL_PATH = "pytorch"

# ──────────────
# 2. Clone PyTorch
# ──────────────
if not os.path.isdir(LOCAL_PATH):
    print(f"Cloning {REPO_URL} → {LOCAL_PATH} …")
    Repo.clone_from(REPO_URL, LOCAL_PATH)
else:
    print(f"Using existing clone at ./{LOCAL_PATH}")

# ──────────────
# 3. Read & concatenate all .py files
# ──────────────
print("Reading .py files from the codebase…")
corpus = []
for root, _, files in os.walk(LOCAL_PATH):
    for name in files:
        if name.endswith(".py"):
            full = os.path.join(root, name)
            try:
                with open(full, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                header = f"# ==== File: {full}\n"
                corpus.append(header + text + "\n")
            except Exception:
                # skip unreadable files
                continue

big_text = "\n".join(corpus)
print(f"Total characters read: {len(big_text):,}")

# ──────────────
# 4. Tokenize & trim to last 1,000,000 tokens
# ──────────────
print("Tokenizing with tiktoken and trimming to 1 million tokens…")

try:
    enc = tiktoken.encoding_for_model("accounts/fireworks/models/llama4-maverick-instruct-basic")
except KeyError:
    enc = tiktoken.get_encoding("cl100k_base")

all_tokens = enc.encode(big_text)
MAX_CTX = 1_000_000

if len(all_tokens) > MAX_CTX:
    print(f"Corpus is {len(all_tokens):,} tokens; trimming to {MAX_CTX:,}.")
    trimmed = all_tokens[-MAX_CTX:]
else:
    trimmed = all_tokens
    print(f"Corpus fits within {MAX_CTX:,} tokens ({len(all_tokens):,}).")

prompt_text = enc.decode(trimmed)

# ──────────────
# 5. Call the model with a huge prompt
# ──────────────
print("Sending prompt to LLaMA 4 Maverick (1M‑token window)…")
response = client.chat.completions.create(
    model="accounts/fireworks/models/llama4-maverick-instruct-basic",

# # 1. Global Code-Structure Summary
#     messages = [
#     {"role": "system", "content": "You are an expert code analyst."},
#     {
#         "role": "user",
#         "content": (
#             "I've provided you the entire PyTorch codebase (last 1 million tokens). "
#             "1. List every top‐level package and submodule.\n"
#             "2. Describe the high‐level data‐flow: from Python API calls → C++ core → CUDA kernels.\n"
#             "3. Highlight any cross-module helper functions that are reused in at least three places."
#         ),
#     },
#     {"role": "user", "content": prompt_text},
# ],

# # 2. End-to-End Call-Stack Trace
# messages = [
#     {"role": "system", "content": "You are an expert debugger."},
#     {
#         "role": "user",
#         "content": (
#             "I've provided you the entire PyTorch codebase (last 1 million tokens) plus runtime logs. "
#             "Starting from `torch.Tensor.backward()`, trace through each layer of Python, C++ and CUDA calls, "
#             "and show me the full call sequence with file paths and line numbers."
#         ),
#     },
#     {"role": "user", "content": prompt_text},
# ],



    max_tokens=16384,
    temperature=0.2,
    top_p=1,
    top_k=40,
    presence_penalty=0.0,
    frequency_penalty=0.0,
    # ensure prompt isn’t auto‑truncated below 1M :contentReference[oaicite:1]{index=1}
    prompt_truncate_len=MAX_CTX,
)

# ──────────────
# 6. Show the answer
# ──────────────
print("\n=== Model Response ===\n")
print(response.choices[0].message.content)
# API_KEY    = "fw_3Za9gPiF6MuhoYvn2dHX9wz4"