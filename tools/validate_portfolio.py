import json
import re
from pathlib import Path
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "portfolio" / "catalog.json").read_text(encoding="utf-8"))
assert catalog["schema_version"] == "1.0", "Unsupported catalog schema"
entries = catalog["entries"]
ids = [entry["id"] for entry in entries]
assert len(ids) == len(set(ids)), "Duplicate catalog id"
required = {"id", "title", "activity_type", "summary", "skills", "domains", "results", "status"}
local_project_paths = set()
for entry in entries:
    missing = required - entry.keys()
    assert not missing, f"{entry.get('id')}: missing {sorted(missing)}"
    for rel in entry.get("code", []):
        assert (root / rel).exists(), f"Missing file: {rel}"
        if rel.startswith("projects/"):
            local_project_paths.add(rel.split("/")[1])
assert (root / "projects").is_dir(), "projects/ is missing"
actual_projects = {path.name for path in (root / "projects").iterdir() if path.is_dir()}
assert actual_projects == local_project_paths, (
    f"Catalog/project mismatch: unlisted={actual_projects - local_project_paths}; "
    f"missing={local_project_paths - actual_projects}"
)
for markdown in root.rglob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", markdown.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        relative = unquote(target.split("#", 1)[0])
        assert (markdown.parent / relative).exists(), f"Broken link in {markdown}: {target}"
for path in root.rglob("*.ipynb"):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            assert cell.get("execution_count") is None, f"execution count: {path}"
            assert not cell.get("outputs", []), f"output: {path}"
print(f"OK: {len(entries)} catalog entries; {len(actual_projects)} local projects; all notebooks are output-free.")
