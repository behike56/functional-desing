def get_logger(formatter):
    def logger(first, second):
        print(formatter(first, second))

    return logger


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def doc_format_checker_and_converter(conversion_function, valid_formats):
    """
    この関数は、conversion_function と valid_formats のリストをパラメータとして受け取ります。そして、それ自体が次の2つのパラメータを取る新しい関数を返す必要があります：

    filename: 変換対象ファイルの名前
    content: 変換対象ファイルの内容（本文テキスト）
    filename のファイル拡張子が valid_formats リストに含まれる場合、content に対して conversion_function を呼び出した結果を返す。
    それ以外の場合は、メッセージ "invalid file format" 付きの ValueError を発生させる。
    """

    def wrapper(filename, content):
        if filename.split(".")[-1] in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("invalid file format")

    return wrapper


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
