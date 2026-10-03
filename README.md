# ⚡ AntiGravity Starter Kit — Lean AI Coding Rules & Context Optimizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Token Economy](https://img.shields.io/badge/Tokens-65%25%20Saved-brightgreen.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

> **Stop letting your AI coding assistant bloat memory and hallucinate after 15 minutes of work.**  
> The free **AntiGravity Starter Kit** provides a battle-tested, high-efficiency system architecture designed for **Cursor, Windsurf, Claude Code, and Google Antigravity**.

---

## 🚀 The Problem: The "Context Bloat" Trap
Most developers configure their AI coding agents by dumping 200–500 lines of markdown instructions into `.cursorrules` or `.agent/rules`. 
- **The Result:** The model spends 40% of its context window just reading its own rules on every prompt. It begins hallucinating, forgetting initial instructions, and wasting money on redundant tokens.
- **The Solution:** The **Lean Core (<40 lines)** methodology. The root agent configuration remains razor-thin, executing tasks with zero cognitive overload.

---

## ⚡ Quick Start (30 Seconds)

### Step 1: Copy `AGENTS.md`
Simply copy the provided [`AGENTS.md`](AGENTS.md) into the root directory of your workspace or your AI assistant's instructions directory (e.g., `.cursorrules`, `.agent/rules/`, or `AGENTS.md`).

### Step 2: Inspect Your Rules File
Run our built-in zero-dependency Token Inspector CLI to verify your agent doesn't suffer from memory bloat:

```bash
python3 tools/token_inspector.py AGENTS.md
```

You will get instant feedback on lines, word count, and token efficiency score.

---

## 📊 Free Community vs. Production Suite (Pro)

| Feature | Starter Kit (Free) | [Production Suite (Pro)](https://lemonsqueezy.com) |
| :--- | :---: | :---: |
| **Lean Core AGENTS.md Template** | ✅ Yes (<40 lines) | ✅ Advanced Architecture |
| **CLI Token Inspector** | ✅ Basic CLI | ✅ Full Weekly Tracker & DB |
| **Multi-Agent Orchestration & Sync** | ❌ | ✅ Yes (Subagent delegation) |
| **Automated Backups & Rollback System** | ❌ | ✅ Yes (`.bak` before edits) |
| **Rule Router & Domain Buckets** | ❌ | ✅ Yes (Auto-routing via Python) |
| **Senior UI/UX Design System (Bento Grid)** | ❌ | ✅ Full Design Guidelines |
| **1-Click Suite Installer (`install.sh`)** | ❌ | ✅ Yes (Global & Workspace) |
| **Direct Author Updates & Support** | ❌ | ✅ Lifetime Updates & Discord |

👉 **[Upgrade to AntiGravity Production Suite on Lemon Squeezy](https://lemonsqueezy.com)** to get the entire multi-agent infrastructure ready for production!

---

## 🛠️ Included in this Repository
- [`AGENTS.md`](AGENTS.md) — The ultra-lean root agent rule template.
- [`tools/token_inspector.py`](tools/token_inspector.py) — Lightweight CLI diagnostic script for token bloat.
- [`LICENSE`](LICENSE) — Open source under the permissive MIT license.

---

## 🤝 Contributing & Community
Contributions, bug reports, and suggestions are welcome! Feel free to open an Issue or submit a Pull Request.

⭐ **If you find this repo helpful, please give it a Star! It helps others discover cleaner AI coding workflows.**
