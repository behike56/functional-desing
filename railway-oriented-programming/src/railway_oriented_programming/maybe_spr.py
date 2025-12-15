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


def handle_user_data(user_id: int):
    match find_user(user_id):
        case Some(user):
            print(f"User found: {user.name}")
        case Nothing:
            print("User not found")


def main() -> None:
    handle_user_data(1)
    handle_user_data(4)


if __name__ == "__main__":
    main()
