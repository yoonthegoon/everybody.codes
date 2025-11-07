from os.path import abspath, dirname, join

ROOT_DIR = dirname(dirname(abspath(__file__)))


def get_notes(event: int, quest: int, part: int) -> str:
    file = join(ROOT_DIR, f"notes/everybody_codes_e{event}_q{quest:02}_p{part}.txt")
    with open(file) as f:
        notes = f.read()
    return notes
