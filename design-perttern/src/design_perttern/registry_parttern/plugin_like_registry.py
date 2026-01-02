"""
プラグイン形式のレジストリ
"""

# plugin_registry.py

PLUGINS = {}


def register_plugin(name):
    def decorator(cls):
        PLUGINS[name] = cls
        return cls

    return decorator


def create_plugin(name, **kwargs):
    try:
        cls = PLUGINS[name]
    except KeyError:
        raise ValueError(f"Unknown plugin: {name}")
    return cls(**kwargs)


# 実装例

# from plugin_registry import register_plugin, create_plugin


class BasePlugin:
    def run(self, data):
        raise NotImplementedError


@register_plugin("uppercase")
class UppercasePlugin(BasePlugin):
    def run(self, data: str) -> str:
        return data.upper()


@register_plugin("reverse")
class ReversePlugin(BasePlugin):
    def run(self, data: str) -> str:
        return data[::-1]


# どのプラグインを使うかは文字列で指定
plugin_name = "reverse"
plugin = create_plugin(plugin_name)

print(plugin.run("hello"))  # -> "olleh"

# ---------- 使用例 ----------

# どのプラグインを使うかは文字列で指定
plugin_name = "reverse"
plugin = create_plugin(plugin_name)

print(plugin.run("hello"))  # -> "olleh"
