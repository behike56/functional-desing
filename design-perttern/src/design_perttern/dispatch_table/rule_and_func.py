"""
ルールと関数を使った分岐

- 条件と処理が完全にデータとして扱える（関数型っぽい！）
- 新しい条件を追加しても関数本体はいじらない
"""

rules = [
    (lambda x: x < 0, lambda x: "negative"),
    (lambda x: x == 0, lambda x: "zero"),
    (lambda x: x > 0, lambda x: "positive"),
]


def evaluate(x):
    for cond, action in rules:
        if cond(x):
            return action(x)
