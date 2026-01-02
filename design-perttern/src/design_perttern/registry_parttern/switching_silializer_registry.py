import json
import pickle
from typing import Any, Protocol, Dict


class Serializer(Protocol):
    def dumps(self, obj: Any) -> bytes: ...
    def loads(self, data: bytes) -> Any: ...


SERIALIZERS: Dict[str, Serializer] = {}


def register_serializer(name: str):
    def decorator(serializer: Serializer):
        SERIALIZERS[name] = serializer
        return serializer

    return decorator


def get_serializer(name: str) -> Serializer:
    try:
        return SERIALIZERS[name]
    except KeyError:
        raise ValueError(f"Unknown serializer: {name}")


# ---------- 実装例 ----------


@register_serializer("json")
class JsonSerializer:
    def dumps(self, obj: Any) -> bytes:
        return json.dumps(obj).encode("utf-8")

    def loads(self, data: bytes) -> Any:
        return json.loads(data.decode("utf-8"))


@register_serializer("pickle")
class PickleSerializer:
    def dumps(self, obj: Any) -> bytes:
        return pickle.dumps(obj)

    def loads(self, data: bytes) -> Any:
        return pickle.loads(data)


# ---------- 使用例 ----------


def save(path: str, obj: Any, serializer_name: str):
    serializer = get_serializer(serializer_name)
    with open(path, "wb") as f:
        f.write(serializer.dumps(obj))


def load(path: str, serializer_name: str) -> Any:
    serializer = get_serializer(serializer_name)
    with open(path, "rb") as f:
        return serializer.loads(f.read())


data = {"x": 1, "y": [1, 2, 3]}
save("data.bin", data, "json")
print(load("data.bin", "json"))
