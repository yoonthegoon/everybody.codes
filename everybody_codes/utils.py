from pathlib import Path

ROOT_DIR = Path(__file__).parents[1]


def get_notes(event: int, quest: int, part: int) -> str:
    file = ROOT_DIR / f"notes/everybody_codes_e{event}_q{quest:02}_p{part}.txt"
    with open(file) as f:
        notes = f.read()
    return notes
