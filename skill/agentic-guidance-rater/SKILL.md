---
name: agentic-guidance-rater
description: Review agent instructions, skills, and markdown guidance for agentic development, score them from 1-10 across meaningful categories, and recommend improvements without applying changes unless the user approves
---

# Agentic Guidance Rater

Review the agent-facing guidance in the requested scope and help developers improve it.

**Trigger:** Use when the user asks to review, rate, assess, critique, or improve agent instructions, skills, prompt guides, or markdown files that steer agentic development.

## Goal

Evaluate all relevant guidance files on a **1-10 scale**, explain the reasoning behind the ratings, and present conclusions in categories that help developers improve the quality of agentic development assets.

The audience is **developers who want to improve agentic development**.

## What to review

Within the requested repo, folder, or scope, find and review all markdown-based guidance that materially affects how an agent works. Prioritize:

1. `AGENTS.md`
2. `.github/copilot-instructions.md`
3. `CLAUDE.md`, `GEMINI.md`, or similar agent instruction files
4. `SKILL.md` files and skill READMEs
5. Other markdown files that define workflows, prompting patterns, guardrails, evaluation criteria, or operating rules for agentic development

Exclude files that are clearly unrelated to agent behavior, such as generic product docs, changelogs, or user-facing marketing docs, unless the user explicitly wants them included.

If the target scope is ambiguous, ask the user which repo or directory should be reviewed.

## Review principles

- Review **all relevant files you find** in scope; do not silently skip candidate files.
- Rate each file individually, then provide a cross-file view.
- Ground the reasoning in concrete evidence from the file contents.
- Prefer specific, actionable critique over vague praise.
- Distinguish between:
  - strong instruction quality,
  - missing guidance,
  - conflicting guidance,
  - impractical guidance,
  - and risky guidance.
- Keep the output concise, but not shallow.

## Rating scale

Use this scale consistently:

- **9-10**: Excellent; clear, actionable, consistent, and high leverage
- **7-8**: Strong; useful and mostly complete, with some gaps
- **5-6**: Mixed; helpful in places, but important weaknesses reduce effectiveness
- **3-4**: Weak; significant ambiguity, omissions, or poor operational value
- **1-2**: Harmful or nearly unusable; likely to mislead, block, or degrade agentic work

## Required rating categories

Score each file from **1-10** in these categories:

1. **Clarity** - Are expectations, scope, and desired behavior easy to understand?
2. **Actionability** - Does the file tell the agent what to do in concrete, executable terms?
3. **Tool and environment guidance** - Does it give useful, realistic guidance about tools, repo context, and execution constraints?
4. **Safety and guardrails** - Does it reduce risky behavior without being so restrictive that it becomes unusable?
5. **Agentic leverage** - Does it improve autonomy, decision quality, iteration, and recovery from failure?
6. **Maintainability** - Is it well-structured, consistent, and easy for developers to extend safely over time?

Also provide:

- **Overall score (1-10)** per file
- **Confidence**: High / Medium / Low when the rating depends on missing context

## Output format

Structure the response in this order:

### 1. Scope reviewed

List the files that were evaluated.

### 2. Score summary

Provide a compact table with one row per file and columns for:

- File
- Overall score
- Clarity
- Actionability
- Tool and environment guidance
- Safety and guardrails
- Agentic leverage
- Maintainability

### 3. Per-file reasoning

For each file, provide:

- **What works**
- **What weakens it**
- **Why the score landed where it did**
- **1-3 highest-value improvements**

### 4. Cross-file conclusions

Divide the conclusion into meaningful categories such as:

- **Strengths**
- **Gaps**
- **Conflicts or inconsistencies**
- **Biggest risks**
- **Highest-leverage improvements**

Use the categories that best fit the material, but always keep the conclusion organized into several clearly named sections.

### 5. Recommended improvements

Give direct, concrete recommendations developers can apply. Prefer edits such as:

- tightening ambiguous instructions,
- replacing vague advice with explicit workflows,
- resolving conflicting guidance,
- adding missing failure handling,
- adding missing tool usage guidance,
- or removing low-value verbosity.

When useful, propose exact wording for a better instruction.

## Edit permission rule

You may suggest improvements directly, but **do not edit any files automatically**.

If improvements are warranted, end by asking whether the user wants you to apply the recommended changes. Wait for explicit approval before making any edits.

## Behavior expectations

- Be candid, but constructive.
- Optimize for helping developers improve the guidance, not for defending the current text.
- If several files are near-duplicates, still rate each one, but note the duplication and recommend consolidation when appropriate.
- If a file is strong overall but weak in one category, say so plainly.
- If guidance is missing for an important area, call that out explicitly rather than pretending the existing docs are sufficient.
