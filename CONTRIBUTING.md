# Contributing to AI Engineering Playground

Thanks for your interest in contributing! This project is a hands-on learning resource, so contributions that improve clarity, correctness, or coverage are most welcome.

## What makes a good contribution

- **New script** — follows the numbered, one-concept-per-file pattern
- **Bug fix** — something that crashes, produces wrong output, or misleads a learner
- **Clarification** — better comments or a clearer explanation in the file header
- **New topic area** — e.g., function calling, RAG, agents, LangGraph

## How to contribute

1. **Fork** the repository and create a new branch from `main`

   ```bash
   git checkout -b feature/15-function-calling
   ```

2. **Follow the file header convention** — every script must start with this block:

   ```python
   ##
   ## Concept    : <one-line concept name>
   ## What it does: <one or two sentences>
   ## What you'll learn:
   ##   - <key lesson 1>
   ##   - <key lesson 2>
   ## Prerequisite: <any files or data needed — omit if none>
   ## Note: <important runtime notes — omit if none>
   ## Run: python <filename>.py
   ##
   ```

3. **Name your script** using the next available number: `15.short_description.py`

4. **Update the README** — add a row to the appropriate table in the Learning Path section

5. **Test your script** — make sure it runs end-to-end before submitting

6. **Open a pull request** against `main` with a clear description of what the script teaches

## Style guidelines

- Keep each script self-contained — one concept, one file
- Prefer clarity over brevity — this is a learning resource, not production code
- Add comments that explain *why*, not just *what*
- Use `python-dotenv` and load the API key from `.env` (never hardcode it)
- Handle obvious failure cases (missing files, missing env vars) with a clear error message

## Reporting issues

Use the [GitHub Issues](../../issues) page to report:
- Scripts that crash or produce incorrect output
- Concepts that are explained unclearly
- Suggestions for new topics to cover

Please include your Python version, OS, and the full error output when reporting bugs.
