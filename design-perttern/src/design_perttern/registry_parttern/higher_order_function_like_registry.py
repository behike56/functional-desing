"""
高階関数形式のレジストリ

関数型スタイルを意識すると、

- レジストリ自体を引数として渡す
- グローバルをあまり使わない
"""

from dataclasses import dataclass
from typing import Callable, Dict

Handler = Callable[[str], str]


@dataclass(frozen=True)
class Registry:
    handlers: Dict[str, Handler]

    def add(self, name: str, handler: Handler) -> "Registry":
        new_handlers = dict(self.handlers)
        new_handlers[name] = handler
        return Registry(new_handlers)

    def get(self, name: str) -> Handler:
        try:
            return self.handlers[name]
        except KeyError:
            raise ValueError(f"Unknown handler: {name}")


# ---------- 使用例 ----------


def to_upper(s: str) -> str:
    return s.upper()


def surround_with_brackets(s: str) -> str:
    return f"[{s}]"


# 空のレジストリから段階的に追加（疑似的にイミュータブル）
reg0 = Registry(handlers={})
reg1 = reg0.add("upper", to_upper)
reg2 = reg1.add("bracket", surround_with_brackets)


def apply_handler(registry: Registry, name: str, value: str) -> str:
    handler = registry.get(name)
    return handler(value)


print(apply_handler(reg2, "upper", "hello"))  # HELLO
print(apply_handler(reg2, "bracket", "hello"))  # [hello]
