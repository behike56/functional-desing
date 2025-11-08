import decorators as deco
import functools


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


def join(doc_so_far, sentence):
    return doc_so_far.join(sentence)


def join_first_sentences(sentences, n):
    temp = sentences[:n]
    result = functools.reduce(join, temp)
    return result


def main():
    try:
        test_list = [
            ("user", "goku_fanatic"),
            ("password", "kakarot1989"),
        ]
        deco.args_logger(**dict(test_list))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
