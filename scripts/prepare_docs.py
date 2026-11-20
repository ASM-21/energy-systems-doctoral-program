"""Stage repository Markdown into a clean MkDocs documentation tree."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "site_docs"
SKIP_DIRS = {
    ".git", ".github", ".venv", "venv", "site", "site_docs",
    "node_modules", "__pycache__", ".pytest_cache",
}


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    for source in ROOT.rglob("*.md"):
        relative = source.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        target = DEST / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    count = sum(1 for _ in DEST.rglob("*.md"))
    print(f"Staged {count} Markdown files into {DEST}")


if __name__ == "__main__":
    main()
