import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "portfolio" / "catalog.json").read_text(encoding="utf-8"))
entries = catalog["entries"]
ids = [entry["id"] for entry in entries]
assert len(ids) == len(set(ids)), "Duplicate catalog id"
for entry in entries:
    for rel in entry.get("code", []):
        assert (root / rel).exists(), f"Missing file: {rel}"
for path in root.rglob("*.ipynb"):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            assert cell.get("execution_count") is None, f"execution count: {path}"
            assert not cell.get("outputs", []), f"output: {path}"
print(f"OK: {len(entries)} catalog entries; all notebooks are output-free.")
