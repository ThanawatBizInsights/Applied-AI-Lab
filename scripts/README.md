# Scripts

| Script | Purpose |
|---|---|
| `validate_repo.py` | checks structure, hours, weights, links, instruction consistency, secrets and large files. Exit code 1 on failure. |
| `scaffold.py` | creates week outlines, course READMEs, project workspaces and experiment templates from `data_*.py`. Never overwrites existing files. |
| `data_weeks.py`, `data_projects.py`, `data_experiments.py` | source data for the scaffold |
