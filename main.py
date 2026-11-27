from os import environ
from pathlib import Path
from shutil import copyfile

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "asset.png"


def destination() -> Path:
    out_dir = Path(environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.png"


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def run() -> None:
    if not IMAGE.is_file():
        raise FileNotFoundError(f"missing bundled image: {IMAGE.name}")
    with IMAGE.open("rb") as handle:
        if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            raise ValueError(f"bundled image is not a PNG: {IMAGE.name}")
    target = destination()
    copyfile(IMAGE, target)
    if target.stat().st_size != IMAGE.stat().st_size:
        raise OSError("output image size does not match the bundled image")


if __name__ == "__main__":
    run()
