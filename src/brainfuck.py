import math

# Translate print statement in brainfuck

def letterPrinter(letter: str):
    if len(letter) != 1:
        return ""

    code = ord(letter)
    res = ""
    root = math.floor(math.sqrt(code))
    for _ in range(root):
        res += "+"

    res += "[>"

    for _ in range(root):
        res += "+"

    res += "<-]>"

    for _ in range(code - root ** 2):
        res += "+"

    res += "."
    return res


def stringPrinter(s: str):
    res = ""
    for letter in s:
        res += letterPrinter(letter)
        res += ">\n"

    return res
