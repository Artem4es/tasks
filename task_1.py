from collections import deque


def check_relation(net: tuple[tuple[str]], first: str, second: str) -> bool:
    """Check if first and second are friends or have common friend"""
    queue: deque = deque()
    queue.append(first)
    checked_names: list[str] = []

    while queue:
        person: str = queue.popleft()
        checked_names.append(person)
        for el in net:
            if person in el:
                person_idx: int = el.index(person)
                friend_idx: int = (person_idx + 1) % 2
                friend: str = el[friend_idx]
                if friend not in checked_names:
                    if friend == second:
                        return True
                    queue.append(friend)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"),
        ("Лёша", "Катя"),
        ("Ваня", "Катя"),
        ("Вова", "Катя"),
        ("Лёша", "Лена"),
        ("Оля", "Петя"),
        ("Стёпа", "Оля"),
        ("Оля", "Настя"),
        ("Настя", "Дима"),
        ("Дима", "Маша"),
    )
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
