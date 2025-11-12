from itertools import chain, tee


def get_names_rules(notes: str) -> tuple[list[str], list[str]]:
    names_str, rules_str = notes.split("\n\n")
    names = names_str.split(",")
    rules = rules_str.split("\n")
    return names, rules


def get_name_pairs(name: str) -> list[str]:
    a, b = tee(name)
    next(b, None)
    return list(map("".join, zip(a, b)))


def get_rule_pairs(rule: str) -> list[str]:
    pairs = []
    a, bs_str = rule.split(" > ")
    for b in bs_str.split(","):
        pairs.append(a + b)
    return pairs


def validate_name(name: str, rules: list[str]) -> bool:
    name_pairs = get_name_pairs(name)
    rule_pairs = list(chain.from_iterable(map(get_rule_pairs, rules)))
    for name_pair in name_pairs:
        if name_pair not in rule_pairs:
            return False
    return True


def p1(notes: str) -> str:
    names, rules = get_names_rules(notes)
    for name in names:
        if validate_name(name, rules):
            return name
    raise ValueError("Invalid notes")


def p2(notes: str) -> int:
    acc = 0
    names, rules = get_names_rules(notes)
    for i, name in enumerate(names, 1):
        if validate_name(name, rules):
            acc += i
    return acc


# TODO: do this faster
def p3(notes: str) -> int:
    names, rules = get_names_rules(notes)
    filtered_names = []
    for name in names:
        if validate_name(name, rules):
            filtered_names.append(name)
    filtered_rules = list(filter(lambda r: r == r.lower(), rules))
    unique_names = set()

    def dfs(name_: str):
        if name_ in unique_names:
            return
        if len(name_) >= 7:
            unique_names.add(name_)
        if len(name_) >= 11:
            return
        for rule in filtered_rules:
            if rule[0] != name_[-1]:
                continue
            rule_pairs = get_rule_pairs(rule)
            for rule_pair in rule_pairs:
                dfs(name_ + rule_pair[-1])

    for name in filtered_names:
        dfs(name)

    return len(unique_names)


if __name__ == "__main__":
    from everybody_codes.utils import get_notes

    p1_notes = get_notes(2025, 7, 1)
    p1_answer = p1(p1_notes)
    print(p1_answer)

    p2_notes = get_notes(2025, 7, 2)
    p2_answer = p2(p2_notes)
    print(p2_answer)

    p3_notes = get_notes(2025, 7, 3)
    p3_answer = p3(p3_notes)
    print(p3_answer)
