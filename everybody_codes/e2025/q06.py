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


# TODO: do this prettier lmao
def p3(notes: str) -> int:
    notes_len = len(notes)
    pairs = {"begin": 0, "middle": 0, "end": 0}
    mentors = {"A": 0, "B": 0, "C": 0}
    novices = {"a": 0, "b": 0, "c": 0}

    def acc_pairs(j_: int, phase_: str):
        _j_ = j_ % notes_len
        for m_, n_ in ("Aa", "Bb", "Cc"):
            if notes[_j_] == m_:
                mentors[m_] += 1
                pairs[phase_] += novices[n_]
            elif notes[_j_] == n_:
                novices[n_] += 1
                pairs[phase_] += mentors[m_]

    for j in range(1001):
        acc_pairs(j, "begin")

    i, j = 0, 1000
    while j < 3 * notes_len - 1:
        if i < notes_len:
            phase = "begin"
        elif i < 2 * notes_len:
            phase = "middle"
        else:
            phase = "end"

        _i = i % notes_len
        for m, n in ("Aa", "Bb", "Cc"):
            if notes[_i] == m:
                mentors[m] -= 1
            if notes[_i] == n:
                novices[n] -= 1
        i += 1
        j += 1
        acc_pairs(j, phase)
    return pairs["begin"] + 998 * pairs["middle"] + pairs["end"]


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
