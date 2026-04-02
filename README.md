# copilot-skills

A collection of small, reusable Python utilities for everyday tasks.

## Modules

| Module | Description |
|---|---|
| `skills.string_utils` | Slug generation, truncation, case conversion, HTML stripping |
| `skills.file_utils` | Directory creation, JSON read/write, recursive file search |
| `skills.date_utils` | Day differences, week boundaries, weekend detection, friendly dates |

## Quick start

```bash
pip install -r requirements.txt
```

```python
from skills import slugify, friendly_date, ensure_dir

print(slugify("Hello World!"))      # hello-world
print(friendly_date(date.today()))  # Today
ensure_dir("output/reports")        # creates the directory tree
```

## Running tests

```bash
pytest
```

## Skills reference

### `string_utils`

| Function | Signature | Description |
|---|---|---|
| `slugify` | `slugify(text)` | URL-friendly slug from any string |
| `truncate` | `truncate(text, max_length, suffix="...")` | Shorten a string with a suffix |
| `camel_to_snake` | `camel_to_snake(name)` | `myVar` → `my_var` |
| `snake_to_camel` | `snake_to_camel(name)` | `my_var` → `myVar` |
| `strip_html` | `strip_html(html)` | Remove all HTML tags |

### `file_utils`

| Function | Signature | Description |
|---|---|---|
| `ensure_dir` | `ensure_dir(path)` | `mkdir -p` equivalent, returns `Path` |
| `read_json` | `read_json(path)` | Parse a JSON file |
| `write_json` | `write_json(path, data, indent=2)` | Write data as pretty JSON |
| `find_files` | `find_files(root, pattern)` | Recursively yield matching files |

### `date_utils`

| Function | Signature | Description |
|---|---|---|
| `days_between` | `days_between(start, end)` | Signed day count between two dates |
| `start_of_week` | `start_of_week(d)` | Monday of the week containing `d` |
| `end_of_week` | `end_of_week(d)` | Sunday of the week containing `d` |
| `is_weekend` | `is_weekend(d)` | `True` on Saturday/Sunday |
| `friendly_date` | `friendly_date(d)` | "Today", "Yesterday", "Tomorrow", or formatted date |
