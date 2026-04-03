# copilot-skills

A collection of daily-use skills: reusable Python utilities and GitHub Copilot agent skills for git worktrees.

---

## Copilot Skills

Copilot skills live in their own directories and each contain a `SKILL.md` that describes the skill's trigger, rules, and step-by-step behaviour.

| Skill | Directory | Description |
|---|---|---|
| **Worktree Lifecycle** | [`worktree-lifecycle/`](worktree-lifecycle/SKILL.md) | Spin up a new branch worktree, do work inside it, then confirm and clean it up |
| **Worktree Cleanup** | [`worktree-cleanup/`](worktree-cleanup/SKILL.md) | Safely remove a finished worktree and optionally delete its local branch |

### Worktree Lifecycle

Trigger: *"spin up a new branch workspace"*, *"create a worktree for …"*

Key steps:
1. Collect branch name (and optional base branch, default `main`)
2. Fetch & update base branch
3. Create worktree + branch via `git worktree add`
4. Optionally open the worktree in VS Code
5. On completion, confirm then remove worktree + optionally delete branch

### Worktree Cleanup

Trigger: *"cleanup this worktree"*, *"finish and remove"*, *"done with this branch workspace"*

Key steps:
1. Validate worktree and repo root paths
2. Show current branch and dirty-state
3. Confirm before removing worktree (`git worktree remove`)
4. Confirm before deleting local branch (`git branch -d/-D`)
5. Prune stale worktree refs

---

## Python Utilities

A small library of helper functions for common everyday tasks.

### Quick start

```bash
pip install -r requirements.txt
```

```python
from datetime import date

from skills import slugify, friendly_date, ensure_dir

print(slugify("Hello World!"))      # hello-world
print(friendly_date(date.today()))  # Today
ensure_dir("output/reports")        # creates the directory tree
```

### Running tests

```bash
pytest
```

### Module reference

#### `string_utils`

| Function | Signature | Description |
|---|---|---|
| `slugify` | `slugify(text)` | URL-friendly slug from any string |
| `truncate` | `truncate(text, max_length, suffix="...")` | Shorten a string with a suffix |
| `camel_to_snake` | `camel_to_snake(name)` | `myVar` → `my_var` |
| `snake_to_camel` | `snake_to_camel(name)` | `my_var` → `myVar` |
| `strip_html` | `strip_html(html)` | Remove all HTML tags |

#### `file_utils`

| Function | Signature | Description |
|---|---|---|
| `ensure_dir` | `ensure_dir(path)` | `mkdir -p` equivalent, returns `Path` |
| `read_json` | `read_json(path)` | Parse a JSON file |
| `write_json` | `write_json(path, data, indent=2)` | Write data as pretty JSON |
| `find_files` | `find_files(root, pattern)` | Recursively yield matching files |

#### `date_utils`

| Function | Signature | Description |
|---|---|---|
| `days_between` | `days_between(start, end)` | Signed day count between two dates |
| `start_of_week` | `start_of_week(d)` | Monday of the week containing `d` |
| `end_of_week` | `end_of_week(d)` | Sunday of the week containing `d` |
| `is_weekend` | `is_weekend(d)` | `True` on Saturday/Sunday |
| `friendly_date` | `friendly_date(d)` | "Today", "Yesterday", "Tomorrow", or formatted date |
