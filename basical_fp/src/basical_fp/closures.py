def word_count_aggregator():
    count = 0

    def count_with(word):
        nonlocal count
        count += len(word.split())
        return count

    return count_with


def new_collection(initial_docs):
    # 初期リストは変更しない：内部でコピーして保持
    close_list = initial_docs.copy()

    def func(doc):
        # 1件ずつ追加（テスト側が add_doc(doc) として呼ぶ）
        close_list.append(doc)
        # 現在のコレクションを返す（参照でもコピーでも可。ここでは参照を返す）
        return close_list

    return func


# def lines_with_sequence(char):
#     def with_char(length):
#         def with_length(doc):
#             return reduce(countchar, doc.split())

#         return with_length

#     return with_char
