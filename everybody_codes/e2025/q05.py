from typing import Optional


class Segment:
    value: int
    left: Optional[int]
    right: Optional[int]
    next: Optional[Segment]

    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    def _construct(self, number: int) -> None:
        if number < self.value and self.left is None:
            self.left = number
        elif number > self.value and self.right is None:
            self.right = number
        elif self.next is None:
            self.next = Segment(number)
        else:
            self.next._construct(number)

    def construct(self, numbers: list[int]) -> None:
        for number in numbers:
            self._construct(number)

    @property
    def quality(self) -> int:
        if self.next is None:
            return self.value
        return int(str(self.value) + str(self.next.quality))

    @property
    def number(self) -> int:
        buff = ""
        if self.left is not None:
            buff += str(self.left)
        buff += str(self.value)
        if self.right is not None:
            buff += str(self.right)
        return int(buff)


class Sword:
    def __init__(self, note: str) -> None:
        identifier_str, numbers_str = note.split(":")
        identifier = int(identifier_str)
        numbers = list(map(int, numbers_str.split(",")))

        self.identifier = identifier
        self.fishbone = Segment(numbers[0])
        self.fishbone.construct(numbers[1:])

    def __lt__(self, other: Sword) -> bool:
        self_segment, other_segment = self.fishbone, other.fishbone
        if self_segment.quality < other_segment.quality:
            return True
        if self_segment.quality > other_segment.quality:
            return False
        while (self_segment is not None) or (other_segment is not None):
            if self_segment.number < other_segment.number:
                return True
            if self_segment.number > other_segment.number:
                return False
            self_segment, other_segment = self_segment.next, other_segment.next
        return self.identifier < other.identifier


def p1(notes: str) -> int:
    sword = Sword(notes)
    return sword.fishbone.quality


def p2(notes: str) -> int:
    swords = [Sword(note) for note in notes.split()]
    return max(swords).fishbone.quality - min(swords).fishbone.quality


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
