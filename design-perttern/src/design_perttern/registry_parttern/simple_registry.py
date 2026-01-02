"""
一番シンプルなレジストリ（辞書）
"""

# 名前 -> 関数 を保存するためのレジストリ
REGISTRY = {}


def register(name):
    """関数をレジストリに登録するためのデコレータ"""

    def decorator(func):
        REGISTRY[name] = func
        return func

    return decorator


def get(name):
    """名前から関数を取得する"""
    try:
        return REGISTRY[name]
    except KeyError:
        raise ValueError(f"'{name}' はレジストリに登録されていません")


# ---------- 使用例 ----------
# from registry import register, get


@register("hello")
def say_hello():
    print("Hello!")


@register("bye")
def say_bye():
    print("Bye!")


# 動的に呼び出せる
command_name = "hello"  # 例えば設定ファイルやユーザー入力から来る
func = get(command_name)
func()  # -> Hello!
