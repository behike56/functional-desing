import decorators as deco


def main():
    try:
        lists = [
            ["Customer ID", "Billed", "Paid"],
            ["1", "100", "100"],
            ["2", "400", "99"],
            ["3", "50", "25"],
        ]

        temp = ""
        for xs in lists:
            temp += ",".join(xs) + "\\n"

        print(("Processing...", temp))

        result = map(lambda x: ",".join(x), lists)
        print(str(result))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
