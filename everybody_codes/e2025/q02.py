import re

type Complex = tuple[int, int]


def add(lhs: Complex, rhs: Complex) -> Complex:
    x1, y1 = lhs
    x2, y2 = rhs
    return x1 + x2, y1 + y2


def mul(lhs: Complex, rhs: Complex) -> Complex:
    x1, y1 = lhs
    x2, y2 = rhs
    return x1 * x2 - y1 * y2, x1 * y2 + y1 * x2


def div(lhs: Complex, rhs: Complex) -> Complex:
    x1, y1 = lhs
    x2, y2 = rhs
    return int(x1 / x2), int(y1 / y2)


def get_xy(notes: str) -> Complex:
    x, y = map(int, re.match(r"A=\[(?P<x>-?\d+),(?P<y>-?\d+)]", notes).groups())
    return x, y


def should_engrave(point: Complex) -> bool:
    r = (0, 0)
    for _ in range(100):
        r = mul(r, r)
        r = div(r, (100000, 100000))
        r = add(r, point)
        if not (-1000000 <= r[0] <= 1000000 and -1000000 <= r[1] <= 1000000):
            return False
    return True


def p1(notes: str) -> str:
    x, y = get_xy(notes)
    r = (0, 0)
    for _ in range(3):
        r = mul(r, r)
        r = div(r, (10, 10))
        r = add(r, (x, y))
    return f"[{r[0]},{r[1]}]"


def p2(notes: str) -> int:
    x, y = get_xy(notes)
    engraved_count = 0
    for dy in range(0, 1010, 10):
        for dx in range(0, 1010, 10):
            point = (x + dx, y + dy)
            if should_engrave(point):
                engraved_count += 1
    return engraved_count


def p3(notes: str) -> int:
    x, y = get_xy(notes)
    engraved_count = 0
    for dy in range(1001):
        for dx in range(1001):
            point = (x + dx, y + dy)
            if should_engrave(point):
                engraved_count += 1
    return engraved_count


if __name__ == "__main__":
    from everybody_codes.utils import get_notes

    p1_notes = get_notes(2025, 2, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 2, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 2, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
