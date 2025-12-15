from dataclasses import dataclass

from returns.maybe import Maybe, Some, Nothing


@dataclass
class User:
    id: int
    name: str


USERS = {
    1: User(id=1, name="John"),
    2: User(id=2, name="Jane"),
    3: User(id=3, name="Jim"),
}


def find_user(id: int) -> Maybe[User]:
    return Some(USERS.get(id)) if id in USERS else Nothing


result = find_user(1).map(lambda user: user.name)
print(result)

result = find_user(4).map(lambda user: user.name)
print(result)
