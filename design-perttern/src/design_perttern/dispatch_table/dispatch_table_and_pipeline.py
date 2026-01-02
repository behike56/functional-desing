from __future__ import annotations
from typing import Any, Callable, Mapping

Json = dict[str, Any]
Record = Mapping[str, Any]
Stage = Callable[[Json], Json]


# ---------- 関数型っぽいユーティリティ ----------


def pipe(value: Any, *funcs: Callable[[Any], Any]) -> Any:
    """左から順に関数適用していくパイプライン。"""
    for f in funcs:
        value = f(value)
    return value


def deep_merge(left: Json, right: Json) -> Json:
    """
    再帰的にdictをマージ（right優先）。
    listの扱いは要件次第（ここでは上書き）。
    """
    merged: Json = dict(left)
    for k, v in right.items():
        if k in merged and isinstance(merged[k], dict) and isinstance(v, dict):
            merged[k] = deep_merge(merged[k], v)
        else:
            merged[k] = v
    return merged


def merge_with(patch: Json) -> Stage:
    """既存JSONにpatchをdeep mergeするステージを返す。"""
    return lambda base: deep_merge(base, patch)


# ---------- ドメイン：入力からJSONを組み立てる ----------


def classify_kind(record: Record) -> str:
    """
    ディスパッチキーを決める関数。
    例: record["type"] や条件判定の結果を返す。
    """
    return str(record.get("type", "default"))


def build_common(record: Record) -> Json:
    """どのデータでも入る共通部分。"""
    return {
        "meta": {
            "source": record.get("source", "unknown"),
            "timestamp": record.get("timestamp"),
        },
        "id": record.get("id"),
    }


def build_variant_purchase(record: Record) -> Json:
    """type == 'purchase' のときに足す差分。"""
    return {
        "event": {
            "name": "purchase",
            "amount": record.get("amount"),
            "currency": record.get("currency", "JPY"),
        }
    }


def build_variant_signup(record: Record) -> Json:
    """type == 'signup' のときに足す差分。"""
    return {
        "event": {
            "name": "signup",
            "plan": record.get("plan", "free"),
        }
    }


def build_variant_default(record: Record) -> Json:
    """どれにも当てはまらないときの差分。"""
    return {
        "event": {
            "name": "unknown",
            "raw_type": record.get("type"),
        }
    }


# ディスパッチテーブル（キー -> 差分ビルダー）
VARIANT_BUILDERS: dict[str, Callable[[Record], Json]] = {
    "purchase": build_variant_purchase,
    "signup": build_variant_signup,
    "default": build_variant_default,
}


def select_variant_builder(record: Record) -> Callable[[Record], Json]:
    key = classify_kind(record)
    return VARIANT_BUILDERS.get(key, VARIANT_BUILDERS["default"])


# ---------- パイプラインのステージ例 ----------


def validate_required(record: Record) -> Record:
    """必要項目チェック（例）。"""
    if "id" not in record:
        raise ValueError("record must contain 'id'")
    return record


def finalize(json_obj: Json) -> Json:
    """最終整形（不要キー削除など）。"""

    # 例: Noneを落とす
    def drop_none(x: Any) -> Any:
        if isinstance(x, dict):
            return {k: drop_none(v) for k, v in x.items() if v is not None}
        if isinstance(x, list):
            return [drop_none(v) for v in x]
        return x

    return drop_none(json_obj)


def assemble_json(record: Record) -> Json:
    """
    record -> json を「パイプライン×ディスパッチ」で組み立てる本体。
    """
    variant_builder = select_variant_builder(record)

    return pipe(
        record,
        validate_required,
        lambda r: {},  # ベース
        merge_with(build_common(record)),
        merge_with(variant_builder(record)),
        finalize,
    )


# ---------- 使用例 ----------
if __name__ == "__main__":
    rec = {
        "id": "u-1",
        "type": "purchase",
        "amount": 1200,
        "source": "web",
        "timestamp": "2026-01-01T10:00:00+09:00",
    }
    print(assemble_json(rec))
