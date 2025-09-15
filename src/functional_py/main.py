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
    print(result3)


if __name__ == "__main__":
    main()
