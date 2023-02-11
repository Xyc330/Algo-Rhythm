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



# Stolen from github
# Except it doesn't support inputs (,)


def evaluate(code):
    code     = cleanup(list(code))
    bracemap = buildbracemap(code)
    
    cells, codeptr, cellptr = [0], 0, 0
    res = ""

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
        if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
        if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
        if command == ".": res += chr(cells[cellptr])

        
        codeptr += 1
    
    return res


def cleanup(code):
     return ''.join(filter(lambda x: x in ['.', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap
