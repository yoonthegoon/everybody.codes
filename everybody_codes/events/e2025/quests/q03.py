def get_crates(notes: str) -> list[int]:
    return list(map(int, notes.split(",")))


def p1(notes: str) -> int:
    crates = get_crates(notes)
    return sum(set(crates))


def p2(notes: str) -> int:
    crates = get_crates(notes)
    return sum(sorted(set(crates))[:20])


def p3(notes: str) -> int:
    crates = get_crates(notes)
    return max([crates.count(crate) for crate in set(crates)])


if __name__ == "__main__":
    from everybody_codes.utils import get_notes

    p1_notes = get_notes(2025, 3, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 3, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 3, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
