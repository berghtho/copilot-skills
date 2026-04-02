---
name: worktree-lifecycle
description: Create a branch worktree for focused work, operate inside it, and safely clean it up with explicit confirmation
---

# Worktree Lifecycle

Manage a full worktree session from start to finish:

1) ask for branch/worktree name,  
2) create worktree from a base branch,  
3) do work in that worktree context,  
4) on completion, confirm and clean up (remove worktree + optional branch delete).

**Trigger:** Use when the user wants to “spin up” a new branch workspace quickly and clean it up afterward.

## Rules

- Always ask before destructive actions.
- Never delete a worktree or branch without explicit user confirmation.
- Prefer `git -C <path> ...` over relying on persistent `cd`.
- Treat directory context as non-persistent between commands.
- Use safe defaults:
  - default base branch: `main`
  - branch deletion mode: safe delete (`git branch -d`), only use force delete (`-D`) if user explicitly confirms.
- If checks fail, explain why and propose the next command.

## Inputs to collect

Ask the user:

1. **Branch name** (required), e.g. `feat/copilot-worktree-skill`
2. **Base branch** (optional, default: `main`)
3. **Open in VS Code after creation?** (default: yes)

## Derived paths

After finding repo root:

- `repoRoot = git rev-parse --show-toplevel`
- `repoName = basename(repoRoot)`
- `safeBranch = branchName` with `/` and `\` replaced by `-`
- `worktreePath = <parent-of-repoRoot>/<repoName>-<safeBranch>`

Example:
- repo root: `C:\dev\myrepo`
- branch: `feat/logging/fix-timeout`
- worktree path: `C:\dev\myrepo-feat-logging-fix-timeout`

## Creation flow (execute in order)

1. Verify repo:
   - `git rev-parse --show-toplevel`
   - if not in repo: stop and ask user to run from a git repository.

2. Fetch and validate base:
   - `git -C <repoRoot> fetch --all --prune`
   - verify base exists locally or on origin.
   - if only remote exists, create local tracking branch.

3. Update base safely:
   - `git -C <repoRoot> switch <baseBranch>`
   - `git -C <repoRoot> pull --ff-only`

4. Preflight checks:
   - fail if branch already exists locally and is checked out in another worktree.
   - fail if `worktreePath` already exists.

5. Create worktree + new branch:
   - `git -C <repoRoot> worktree add "<worktreePath>" -b "<branchName>" "<baseBranch>"`

6. Confirm success:
   - show created branch + worktree path.
   - optionally open VS Code:
     - `code -r "<worktreePath>"`

## Working phase behavior

- For status/log/commit operations in this session, target the worktree explicitly:
  - `git -C "<worktreePath>" status`
  - `git -C "<worktreePath>" add ...`
  - `git -C "<worktreePath>" commit ...`
  - etc.
- If asked to run non-git commands, run them in the worktree directory context.

## Completion + cleanup flow

When user indicates done (e.g., “done”, “cleanup”, “finish this worktree”):

1. Show current state:
   - `git -C "<worktreePath>" status --short`
   - `git -C "<worktreePath>" branch --show-current`

2. Ask confirmation:
   - “Remove worktree `<worktreePath>` now? (Y/N)”

3. If yes, remove worktree:
   - if clean:
     - `git -C "<repoRoot>" worktree remove "<worktreePath>"`
   - if dirty:
     - warn user and ask:
       - cancel cleanup, or
       - force-remove/discard (only if explicitly confirmed).

4. Ask branch deletion confirmation:
   - “Also delete local branch `<branchName>`? (Y/N)”
   - if yes:
     - try safe delete:
       - `git -C "<repoRoot>" branch -d "<branchName>"`
     - if not fully merged, explain and ask whether to force:
       - `git -C "<repoRoot>" branch -D "<branchName>"` (only with explicit confirmation)

5. Final housekeeping:
   - `git -C "<repoRoot>" worktree prune`
   - report completed cleanup steps.

## Error handling

- If branch already exists:
  - offer choices:
    1) choose another name,
    2) create worktree from existing branch (without `-b`) if not checked out elsewhere.
- If branch is already checked out in another worktree:
  - show `git -C "<repoRoot>" worktree list` and ask user whether to reuse/remove existing one.
- If base branch missing:
  - ask user to provide a valid base branch.
- If path exists:
  - ask whether to choose a new branch name or custom path suffix.

## Response style

- Keep responses concise and action-oriented.
- Before each critical step, state what you are about to do.
- After each command group, summarize result in one short line.
- Always ask before destructive operations.