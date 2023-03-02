formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
the_string = str()


def bold_formatter():
    bold_result = "**" + input("Text: ") + "**"
    global the_string
    the_string += bold_result
    print(the_string)


def italic_formatter():
    italic_result = "*" + input("Text: ") + "*"
    global the_string
    the_string += italic_result
    print(the_string)


def header_formatter():
    level_input = int(input("Level: "))
    if level_input < 1 or level_input > 6:
        print("The level should be within the range of 1 to 6")
        header_formatter()
    else:
        header_result = "#" * level_input + " " + input("Text: ")
        global the_string
        the_string += header_result + "\n"
        print(the_string)


def plain_formatter():
    plain_result = input("Text: ")
    global the_string
    the_string += plain_result
    print(plain_result)


def inline_formatter():
    inline_result = input("Text: ")
    global the_string
    the_string += "`" + inline_result + "`"
    print(the_string)


def new_formatter():
    global the_string
    the_string += "\n"
    print(the_string)


def link_formatter():
    global the_string
    the_string += "[" + input("Label: ") + "]" + "(" + input("URL: ") + ")"
    print(the_string)


def ordered_formatter():
    c = 0
    rows_input = int(input("Number of rows: "))
    if rows_input < 1:
        print("The number of rows should be greater than zero")
        ordered_formatter()
    else:
        global the_string
        while rows_input != 0:
            global the_string
            c += 1
            rows_input -= 1
            the_string += str(c) + ". " + input(f'Row #{c}: ') + "\n"
        print(the_string)


def unordered_formatter():
    c = 0
    rows_input = int(input("Number of rows: "))
    if rows_input < 1:
        print("The number of rows should be greater than zero")
        ordered_formatter()
    else:
        global the_string
        while rows_input != 0:
            c += 1
            rows_input -= 1
            unordered_input = input(f'Row #{c}: ')
            the_string += "* " + unordered_input + "\n"
        print(the_string)


while True:
    a = input("Choose a formatter: ")
    if a == "bold":
        bold_formatter()
        continue
    if a == "italic":
        italic_formatter()
        continue
    if a == "header":
        header_formatter()
        continue
    if a == "plain":
        plain_formatter()
        continue
    if a == "inline-code":
        inline_formatter()
        continue
    if a == "new-line":
        new_formatter()
        continue
    if a == "link":
        link_formatter()
        continue
    if a == "ordered-list":
        ordered_formatter()
        continue
    if a == "unordered-list":
        unordered_formatter()
        continue
    elif a == "!done":
        with open('output.md', 'w') as f:
            f.write(the_string)
        break
    elif a == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    else:
        print("Unknown formatting type or command")
