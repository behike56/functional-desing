def factorial_r(x):
    if x == 0:
        return 1
    return x * factorial_r(x - 1)


def zipmap(keys, values):
    # ベースケース（終了条件）:
    if not keys or not values:
        return {}  # 空の辞書を返す

    # 再帰ステップ:
    # 先頭要素を取り出して、残りを再帰的に処理
    return {keys[0]: values[0]} | zipmap(keys[1:], values[1:])


def sum_nested_list(lst):
    """
    sum of nested list
    lst = [
        5,
        [6, 7],
        [[8, 9], 10]
    ]
    """

    # ベースケース：リストが空なら合計は0
    if not lst:
        return 0

    head, *tail = lst  # 先頭と残りに分解

    # 先頭がリストなら再帰的に合計を求め、
    # そうでなければ値をそのまま足す
    if isinstance(head, list):
        return sum_nested_list(head) + sum_nested_list(tail)
    else:
        return head + sum_nested_list(tail)


def list_files(parent_directory, current_filepath=""):
    """
    parent_directory = {
            "Documents": {
                "Proposal.docx": None,
                "Receipts": {
                    "January": {"receipt1.txt": None, "receipt2.txt": None},
                    "February": {"receipt3.txt": None},
                },
            },
        }
    """
    return [
        # ファイル（valueがNoneのとき）
        current_filepath + key
        for key, value in parent_directory.items()
        if value is None
    ] + [
        # サブディレクトリを再帰的に探索
        file
        for key, value in parent_directory.items()
        if isinstance(value, dict)
        for file in list_files(value, current_filepath + key + "/")
    ]
