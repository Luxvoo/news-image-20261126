from os import environ
from pathlib import Path
from shutil import copyfile

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "asset.png"


def destination() -> Path:
    out_dir = Path(environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.png"


def run() -> None:
    copyfile(IMAGE, destination())


if __name__ == "__main__":
    run()
