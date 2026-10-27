"""Remove execution outputs while preserving notebook source and Markdown."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
changed = 0
for path in root.rglob("*.ipynb"):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    dirty = False
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            if cell.get("outputs"):
                cell["outputs"] = []
                dirty = True
            if cell.get("execution_count") is not None:
                cell["execution_count"] = None
                dirty = True
    if dirty:
        path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        changed += 1
print(f"Cleared outputs in {changed} notebook(s).")
