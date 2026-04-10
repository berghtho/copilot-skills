# copilot-skills

A skill vault of GitHub Copilot agent skills plus a small Python helper library. Skills are reference material, not automation; keep them concise, current, and easy to reuse.

---

## Repository layout

- `skill/<name>/SKILL.md` — Copilot skills with triggers, rules, and step-by-step behaviour
- `skills/` — Python helper library for daily utilities
- `tests/` — pytest coverage for the helper library

## Copilot skills

| Skill | Directory | Description |
|---|---|---|
| **Optimizing EF Core Queries** | [`optimizing-ef-core-queries/`](optimizing-ef-core-queries/SKILL.md) | Diagnose and fix EF Core query performance: N+1 patterns, tracking modes, compiled queries, and common pitfalls |
| **Agentic Guidance Rater** | [`skill/agentic-guidance-rater/`](skill/agentic-guidance-rater/SKILL.md) | Review and score agent instructions and skills, recommending improvements |
| **Worktree Lifecycle** | [`skill/worktree-lifecycle/`](skill/worktree-lifecycle/SKILL.md) | Spin up a new branch worktree, do work inside it, then confirm and clean it up |
| **Worktree Cleanup** | [`skill/worktree-cleanup/`](skill/worktree-cleanup/SKILL.md) | Safely remove a finished worktree and optionally delete its local branch |

When adding a new skill, create `skill/<name>/SKILL.md` with frontmatter (`name`, `description`) and update the table above.

---

## Python utilities

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
