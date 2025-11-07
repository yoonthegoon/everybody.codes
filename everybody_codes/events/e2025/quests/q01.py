from everybody_codes.utils import get_notes


def get_names_instructions(notes: str) -> tuple[list[str], list[str]]:
    names_str, instructions_str, *_ = notes.split("\n\n")
    names = names_str.split(",")
    instructions = instructions_str.split(",")

    return names, instructions


def get_letter_number(instruction: str) -> tuple[str, int]:
    letter, number = instruction[0], int(instruction[1:])
    return letter, number


def p1(notes: str) -> str:
    names, instructions = get_names_instructions(notes)

    max_i = len(names) - 1
    i = 0
    for instruction in instructions:
        letter, number = get_letter_number(instruction)

        if letter == "R":
            i += number
            i = min(i, max_i)
        else:
            i -= number
            i = max(i, 0)

    return names[i]


def p2(notes: str) -> str:
    names, instructions = get_names_instructions(notes)

    i = 0
    for instruction in instructions:
        letter, number = get_letter_number(instruction)

        if letter == "R":
            i += number
        else:
            i -= number

    return names[i % len(names)]


def p3(notes: str) -> str:
    names, instructions = get_names_instructions(notes)

    names_len = len(names)
    i = 0
    for instruction in instructions:
        letter, number = get_letter_number(instruction)

        if letter == "R":
            j = (i + number) % names_len
        else:
            j = (i - number) % names_len
        names[0], names[j] = names[j], names[0]

    return names[0]


if __name__ == "__main__":
    p1_notes = get_notes(2025, 1, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 1, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 1, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
