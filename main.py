"""Family scene entry for make.fun: Make the AI Judge Feel Proud.

The program writes one short family scene (one or two lines, at most
280 characters) to /output/entry.txt, where the bounty judge reads it.
The scene is fixed and deterministic: the same text every run.
"""

from pathlib import Path

SCENE = (
    "Every night Dad texts the family group a photo of the porch light "
    "he leaves on \u2014 'in case you ever need to find your way home.' "
    "I'm thirty-four and live two streets away, and I still check that "
    "light before I sleep."
)

MAX_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    scene = SCENE.strip()
    if not scene:
        raise SystemExit("scene is empty")
    if len(scene) > MAX_CHARS:
        raise SystemExit(
            f"scene is {len(scene)} characters, over the {MAX_CHARS} limit"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(scene + "\n", encoding="utf-8")
    print(f"wrote {len(scene)} characters to {OUTPUT_PATH}")
    print(scene)


if __name__ == "__main__":
    main()
