# copilot-skills

A collection of reusable Copilot skills for agentic development workflows.

## Skills

### [optimizing-ef-core-queries](./optimizing-ef-core-queries/SKILL.md)

Optimize Entity Framework Core queries by fixing N+1 problems, choosing correct tracking modes, using compiled queries, and avoiding common performance traps.

**Use when:** EF Core queries are slow, generating excessive SQL, or causing high database load.

---

### [agentic-guidance-rater](./agentic-guidance-rater/SKILL.md)

Review agent instructions, skills, and markdown guidance for agentic development, score them from 1–10 across meaningful categories, and recommend improvements without applying changes unless the user approves.

**Use when:** You want to review, rate, assess, critique, or improve agent instructions, skills, prompt guides, or markdown files that steer agentic development.

---

### [worktree-lifecycle](./worktree-lifecycle/SKILL.md)

Create a branch worktree for focused work, operate inside it, and safely clean it up with explicit confirmation.

**Use when:** You want to spin up a new branch workspace quickly and clean it up afterward.

---

### [worktree-cleanup](./worktree-cleanup/SKILL.md)

Safely remove a Git worktree and optionally delete its local branch, always with explicit confirmation.

**Use when:** You are done with a worktree and want to remove it cleanly.
