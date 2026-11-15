# Qwen2.5-Coder Coding Agent

This repository contains the Qwen2.5-Coder-1.5B-Instruct model configuration/tokenizer files together with a separately developed coding-agent application.

## Project layout

The model and coding-agent source are located in:

`Qwen2.5-Coder-1.5B-Instruct/Qwen2.5-Coder-1.5B-Instruct/`

The coding agent is in the `coding_agent/` subdirectory. See its `AGENT_README.md` for usage and setup instructions.

## Restore the tokenizer

To keep the repository transfer manageable, the original `tokenizer.json` is stored as 13 text chunks. Before running the agent or model verification, execute this from the model directory:

```bash
python coding_agent/restore_tokenizer.py
```

The script verifies the reconstructed file against the original SHA-256 hash before writing it. GitHub Actions runs this restoration step before tests.

## Important

- Model weights are not included in this Git repository. Download the original weights from the official Qwen Hugging Face repository.
- The Qwen model files remain subject to their original license and attribution. See the included `LICENSE` and `README.md`.
- The coding agent is a separate software layer; it does not change the model weights.
- Command approval is not an operating-system sandbox. Do not run untrusted project code without proper isolation.

Original model: https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct
Original source repository: https://github.com/911houssem/qween
