---
name: worktree-cleanup
description: Safely remove a Git worktree and optionally delete its local branch, always with explicit confirmation
---

# Worktree Cleanup

Safely clean up a finished worktree session.

**Trigger:** Use when the user says they are done with a worktree (e.g., “cleanup this worktree”, “finish and remove”, “done with this branch workspace”).

## Rules

- Never remove a worktree or delete a branch without explicit confirmation.
- Prefer safe operations first (`branch -d` before `-D`).
- Use `git -C <path> ...` for reliable path targeting.
- If repository root is unclear, ask before proceeding.

## Inputs to collect

Ask for:

1. **Worktree path** (required if not inferable from context)
2. **Repo root path** (if needed for `git worktree remove` / branch deletion)
3. **Whether to delete local branch after removing worktree** (Y/N)

## Cleanup flow

1. **Validate paths**
   - Confirm worktree path exists.
   - Confirm repo root is a git repo:
     - `git -C "<repoRoot>" rev-parse --show-toplevel`

2. **Inspect state**
   - `git -C "<worktreePath>" branch --show-current`
   - `git -C "<worktreePath>" status --porcelain`
   - Report:
     - current branch
     - whether uncommitted changes exist

3. **Confirm worktree removal**
   - Ask:
     - “Remove worktree `<worktreePath>` now? (Y/N)”
   - If dirty, add warning:
     - “Uncommitted changes detected. Remove anyway and discard local changes? (Y/N)”

4. **Remove worktree**
   - Clean
