from math import ceil


def get_gears(notes: str) -> list[int]:
    gears = list(map(int, notes.split()))
    return gears


def p1(notes: str) -> int:
    gears = get_gears(notes)
    return int(2025 * gears[0] / gears[-1])


def p2(notes: str) -> int:
    gears = get_gears(notes)
    return ceil(10000000000000 * gears[-1] / gears[0])


def p3(notes: str) -> int:
    gear_pairs_str = notes.split("|")
    turns = 100.0
    for gear_pair_str in gear_pairs_str:
        x, y = map(int, gear_pair_str.split())
        turns *= x / y
    return int(turns)


if __name__ == "__main__":
    from everybody_codes.utils import get_notes

    p1_notes = get_notes(2025, 4, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 4, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 4, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
