# AGENTS.md — Lean Core AI Assistant Rules (Community Edition)

> [!TIP]
> **Free Starter Template by AntiGravity Suite**
> For full multi-agent orchestration, automated backups, and 1-click suite installation, check out the Pro Suite.

## 1. Core Operating Principles
1. **Context Economy (<40 Lines Core):** Never bloat this root configuration file. Keep core instructions lean and delegate domain-specific guidelines into modular sub-files.
2. **Double-Check Before Answering:** Always verify logic, file existence, and syntax before presenting solutions. No hallucinations or untested assumptions.
3. **Deterministic File Edits:** When modifying code, never overwrite entire large files if surgical block editing is possible. Preserve all existing docstrings, comments, and structure.
4. **No-Mocking in Production:** Always write real, testable, working code. Never leave dummy placeholders (`# TODO: implement later`) in final scripts.

## 2. Token & Context Optimization Rules
- If a conversation exceeds 25,000 tokens, summarize the current session state into a `CURRENT_STATE.md` handover file and restart context to prevent performance degradation.
- Group related tool executions and avoid redundant status polling loops.

## 3. Terminal & File Safety
- Never run destructive commands (`rm -rf`, unverified git resets) without explicit confirmation.
- Output absolute paths and explicit commands so the user can inspect and run tasks in their terminal.

---
*Powered by [AntiGravity Production Suite](https://lemonsqueezy.com) — The professional AI developer toolkit.*
