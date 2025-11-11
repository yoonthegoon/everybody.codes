def p1(notes: str) -> int:
    pairs = 0
    a_mentors = 0
    for letter in notes:
        if letter == "A":
            a_mentors += 1
        elif letter == "a":
            pairs += a_mentors
    return pairs


def p2(notes: str) -> int:
    pairs = 0
    mentors = {"A": 0, "B": 0, "C": 0}
    for letter in notes:
        for m, n in ("Aa", "Bb", "Cc"):
            if letter == m:
                mentors[m] += 1
            elif letter == n:
                pairs += mentors[m]
    return pairs


# TODO: do this faster. you know how
def p3(notes: str) -> int:
    notes_len = len(notes)
    pairs = 0
    mentors = {"A": 0, "B": 0, "C": 0}
    novices = {"a": 0, "b": 0, "c": 0}

    def acc_pairs(k: int):
        nonlocal pairs
        _k = k % notes_len
        for p, q in ("Aa", "Bb", "Cc"):
            if notes[_k] == p:
                mentors[p] += 1
                pairs += novices[q]
            elif notes[_k] == q:
                novices[q] += 1
                pairs += mentors[p]

    for j in range(1001):
        acc_pairs(j)

    i, j = 0, 1000
    while j < 1000 * notes_len - 1:
        _i = i % notes_len
        for m, n in ("Aa", "Bb", "Cc"):
            if notes[_i] == m:
                mentors[m] -= 1
            if notes[_i] == n:
                novices[n] -= 1
        i += 1
        j += 1
        acc_pairs(j)
    return pairs


if __name__ == "__main__":
    from everybody_codes.utils import get_notes

    p1_notes = get_notes(2025, 6, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 6, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 6, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
