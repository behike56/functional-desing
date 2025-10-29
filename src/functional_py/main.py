import recursive as recur
import closures as clos
import decorators as deco


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
        deco.args_logger("hi", True, f_name="Lane", l_name="Wagner", age=28)
        # test_dict = {
        #     "a": 1,
        #     "b": 2,
        #     "c": 3,
        #     "d": 4,
        #     "e": 5,
        #     "f": 6,
        #     "g": 7,
        # }

        # sorted_items = sorted(test_dict.items())
        # for key, value in sorted_items:
        #     print(f"{key}: {value}")
        test_list = [
            ("user", "goku_fanatic"),
            ("password", "kakarot1989"),
        ]
        for key, value in test_list:
            print(f"{key}: {value}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
