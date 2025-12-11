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


def find_longest_word(document, longest_word=""):
    if document == "":
        return longest_word

    doc = document.split(" ")
    if len(doc[0]) > len(longest_word):
        longest_word = doc[0]

    return find_longest_word(" ".join(doc[1:]), longest_word)


def count_nested_levels(nested_documents, target_document_id, level=1):
    """
    ネストされた辞書の中で target_document_id が現れる深さを返す。
    見つからない場合は None を返す。
    {
        1: {
            3: {}
        },
        2: {}
    },
    """

    for key, value in nested_documents.items():
        if key == target_document_id:
            return level  # 見つかったら現在のレベルを返す

        # value が辞書なら再帰的に探索
        if isinstance(value, dict):
            result = count_nested_levels(value, target_document_id, level + 1)
            if result != -1:
                return result  # 見つかった場合のみ返す

    # この階層には見つからなかった
    return -1
