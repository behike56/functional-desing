def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper


@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"


def args_logger(*args, **kwargs):
    idx = 1
    for arg in args:
        print(f"{idx}. {arg}")
        idx += 1

    for key, val in sorted(kwargs.items()):
        print(f"* {key}: {val}")


def configure_plugin_decorator(func):
    def wrapper(*args):
        kwargs = {}
        for key, value in args:
            kwargs[key] = value
        return func(**kwargs)

    return wrapper


@configure_plugin_decorator
def configure_backups(path="~/backups", prefix="copy_", extension=".txt"):
    return {
        "path": path,
        "prefix": prefix,
        "extension": extension,
    }


@configure_plugin_decorator
def configure_login(user=None, password=None, token=None):
    return {
        "user": user,
        "password": password,
        "token": token,
    }
