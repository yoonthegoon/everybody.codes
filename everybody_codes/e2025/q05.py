from typing import Optional


class Segment:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.bottom = None

    def __lt__(self, other: Segment) -> Optional[bool]:
        if self.number < other.number:
            return True
        if self.number > other.number:
            return False
        if self.bottom is None or other.bottom is None:
            return None
        return self.bottom < other.bottom

    def _construct(self, value: int):
        if self.left is None and value < self.value:
            self.left = value
        elif self.right is None and value > self.value:
            self.right = value
        elif self.bottom is None:
            self.bottom = Segment(value)
        else:
            self.bottom._construct(value)

    def construct(self, values: list[int]):
        for value in values:
            self._construct(value)

    @property
    def quality(self) -> str:
        if self.bottom is None:
            return str(self.value)
        return str(self.value) + self.bottom.quality

    @property
    def number(self) -> int:
        number_str = ""
        if self.left is not None:
            number_str += str(self.left)
        number_str += str(self.value)
        if self.right is not None:
            number_str += str(self.right)
        return int(number_str)


class Sword:
    def __init__(self, note: str):
        self.note = note

        identifier_str, numbers_str = note.split(":")
        numbers = list(map(int, numbers_str.split(",")))

        self.identifier = int(identifier_str)
        self.spine = Segment(numbers[0])
        self.spine.construct(numbers[1:])

    def __lt__(self, other: Sword) -> bool:
        if self.quality < other.quality:
            return True
        if self.quality > other.quality:
            return False
        segment_lt = self.spine < other.spine
        if segment_lt is None:
            return self.identifier < other.identifier
        return segment_lt

    @property
    def quality(self) -> int:
        return int(self.spine.quality)


def p1(notes: str) -> int:
    sword = Sword(notes)
    return sword.quality


def p2(notes: str) -> int:
    swords = [Sword(note) for note in notes.split()]
    return max(swords).quality - min(swords).quality


def p3(notes: str) -> int:
    swords = [Sword(note) for note in notes.split()]
    checksum = 0
    for i, sword in enumerate(sorted(swords, reverse=True), 1):
        checksum += i * sword.identifier
    return checksum


if __name__ == "__main__":
    from everybody_codes.utils import get_notes

    p1_notes = get_notes(2025, 5, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 5, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 5, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
