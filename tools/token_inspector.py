#!/usr/bin/env python3
"""
Token Inspector — AntiGravity Community Edition
Quickly inspect prompt & agent configuration files to prevent context bloat.
"""

import sys
import os

def analyze_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.splitlines()
    num_lines = len(lines)
    word_count = len(content.split())
    # Standard heuristic: ~4 characters or ~0.75 words per token in English/Code
    est_tokens = max(1, int(len(content) / 3.8))

    print("==================================================")
    print(f" 🔍 INSPECTION REPORT: {os.path.basename(filepath)}")
    print("==================================================")
    print(f" • File Path:       {filepath}")
    print(f" • Total Lines:     {num_lines}")
    print(f" • Word Count:      {word_count}")
    print(f" • Est. Tokens:     ~{est_tokens:,} tokens")
    print("--------------------------------------------------")

    if num_lines <= 40:
        print(" [STATUS] ✅ LEAN CORE VERIFIED (< 40 lines)")
        print(" Excellent! Your agent will retain maximum context agility.")
    elif num_lines <= 80:
        print(" [STATUS] 🟡 MODERATE SIZE (40 - 80 lines)")
        print(" Consider splitting domain-specific rules into separate files.")
    else:
        print(" [STATUS] 🔴 BLOAT DETECTED (> 80 lines)")
        print(" Warning: Large rule files degrade AI reasoning and waste budget.")

    print("==================================================")
    print(" Need full multi-agent orchestration & automatic token tracking?")
    print(" Check out AntiGravity Production Suite: https://lemonsqueezy.com")
    print("==================================================")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "AGENTS.md"
    analyze_file(target)
