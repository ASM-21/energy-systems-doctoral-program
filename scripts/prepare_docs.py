"""Stage Markdown and selected static assets into a clean MkDocs source tree."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "site_docs"
SKIP_DIRS = {
    ".git", ".github", ".venv", "venv", "site", "site_docs",
    "node_modules", "__pycache__", ".pytest_cache",
}
DOCUMENT_SUFFIXES = {".md"}
ASSET_SUFFIXES = {".csv", ".json", ".png", ".jpg", ".jpeg", ".svg", ".pdf"}


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    copied = 0
    for source in ROOT.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if source.suffix.lower() not in DOCUMENT_SUFFIXES | ASSET_SUFFIXES:
            continue
        target = DEST / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied += 1

    markdown_count = sum(1 for _ in DEST.rglob("*.md"))
    asset_count = copied - markdown_count
    print(
        f"Staged {markdown_count} Markdown files and {asset_count} static assets "
        f"into {DEST}"
    )


if __name__ == "__main__":
    main()
