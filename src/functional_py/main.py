import recursive as recur
import closures as clos


def change_bullet_style(document):
    return "\n".join(list(map(convert_line, document.split("\n"))))


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line


def remove_invalid_lines(document):
    return "\n".join(filter(is_start_with_asta, document.split("\n")))


def is_start_with_asta(line) -> bool:
    if len(line) > 0 and line[0] == "-":
        return False

    return True


import functools


def join(doc_so_far, sentence):
    return doc_so_far.join(sentence)


def join_first_sentences(sentences, n):
    temp = sentences[:n]
    result = functools.reduce(join, temp)
    return result


def main():
    try:
        result1 = change_bullet_style("* Alai\n- Dink Meeker\n")
        # print(result1)

        result2 = remove_invalid_lines(
            "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n",
        )
        # print(result2)

        # ["I don't feel safe", "Are you cussing with me"],
        # 2,
        result3 = join_first_sentences(
            ["I don't feel safe", "Are you cussing with me"],
            2,
        )
        # print(result3)

        a = ["a", "b", "c"]
        b = [1, 2, 3]
        # print(a[-len(a) + 1 : len(a)])
        # print(b[-len(b) + 1 : len(b)])

        # result = recur.zipmap(["a", "b", "c"], [1, 2, 3])
        # print(result)

        # root = [1, 2, [3, 4]]
        # result = recur.sum_nested_list(root)
        # print(result)

        root = {
            "Documents": {
                "Proposal.docx": None,
                "Receipts": {
                    "January": {"receipt1.txt": None, "receipt2.txt": None},
                    "February": {"receipt3.txt": None},
                },
            },
        }
        # result = recur.list_files(root)
        # print(result)
        # temp_list = []
        # temp_list.append("a")
        # print(temp_list)
        #
        # nested_documents = {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}
        # result = recur.count_nested_levels(nested_documents, 9)
        # print(result)
        # nested_documents = {1: {}, 2: {}, 3: {}}
        # for i in nested_documents.items():
        val1 = []
        val2 = [1, 2, 3]
        val1.append(val2)
        val1.append(4)
        val1.append("5")
        print(val1)
        result = clos.new_collection(["Dan Evans"])
        print(result)
        result2 = clos.new_collection(["Charlie Prince"])
        print(result2)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
