# Agent instructions

- Treat this repository as a skill vault. Prefer minimal, surgical edits that keep skills accurate and discoverable.
- All skills live under `skill/<name>/SKILL.md` with `name` and `description` frontmatter. Update the skill table in `README.md` whenever you add, remove, or rename a skill.
- Keep skills self-contained and reference-focused: do not add automation glue or unrelated code. Preserve existing wording unless you are asked to improve it.
- The Python helper library remains in `skills/`. Keep its API stable, avoid new dependencies unless required, and run `pytest` before and after changes.
- Do not commit build artifacts or virtualenvs. Honor `.gitignore` and keep the repo lean.
