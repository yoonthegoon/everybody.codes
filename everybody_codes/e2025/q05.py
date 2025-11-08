from typing import Optional


class Segment:
    value: int
    left: Optional[int] = None
    right: Optional[int] = None
    next: Optional[Segment] = None

    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        buffer = ""
        if self.left is not None:
            buffer += f"{self.left}-"
        else:
            buffer += "  "
        buffer += f"{self.value}"
        if self.right is not None:
            buffer += f"-{self.right}"
        if self.next is not None:
            buffer += f"\n  |\n{self.next}"
        return buffer

    def construct(self, numbers: list[int]) -> None:
        for number in numbers:
            self._construct(number)

    def _construct(self, number: int) -> None:
        if number < self.value and self.left is None:
            self.left = number
        elif number > self.value and self.right is None:
            self.right = number
        elif self.next is None:
            self.next = Segment(number)
        else:
            self.next._construct(number)

    @property
    def level(self) -> int:
        return int("".join(map(str, filter(None, (self.left, self.value, self.right)))))

    @property
    def spine(self) -> int:
        if self.next is None:
            return self.value
        return int(str(self.value) + str(self.next.spine))


class Sword:
    identifier: int
    fishbone: Segment

    def __init__(self, identifier: int, numbers: list[int]) -> None:
        self.identifier = identifier
        self.fishbone = Segment(numbers[0])
        self.fishbone.construct(numbers[1:])

    def __repr__(self) -> str:
        return f"id: {self.identifier}\n\n{self.fishbone}"

    def __lt__(self, other: Sword) -> bool:
        self_segment, other_segment = self.fishbone, other.fishbone
        if self_segment.spine < other_segment.spine:
            return True
        if self_segment.spine > other_segment.spine:
            return False
        while (self_segment is not None) or (other_segment is not None):
            if self_segment.level < other_segment.level:
                return True
            if self_segment.number > other_segment.level:
                return False
            self_segment, other_segment = self_segment.next, other_segment.next
        return self.identifier < other.identifier


def get_identifiers_numbers(notes: str) -> list[tuple[int, list[int]]]:
    identifiers_numbers = []
    for line in notes.split():
        identifier_str, numbers_str = line.split(":")
        identifier = int(identifier_str)
        numbers = list(map(int, numbers_str.split(",")))
        identifiers_numbers.append((identifier, numbers))
    return identifiers_numbers


def p1(notes: str) -> int:
    identifier, numbers = get_identifiers_numbers(notes)[0]
    sword = Sword(identifier, numbers)
    return sword.fishbone.spine


def p2(notes: str) -> int:
    swords = [
        Sword(identifier, numbers)
        for identifier, numbers in get_identifiers_numbers(notes)
    ]
    return max(swords).fishbone.spine - min(swords).fishbone.spine


def p3(notes: str) -> int:
    swords = [
        Sword(identifier, numbers)
        for identifier, numbers in get_identifiers_numbers(notes)
    ]
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
