"""*Compiles Brainfuck programs to Python using Unfuck*
"""

import sys
import os
from unfuck import Unfuck
from datetime import datetime

COMMANDS = {
    "+", "-",
    ">", "<",
    "[", "]",
    ".", ","
}


class NewFile:

    def __init__(self):
        self.filename = datetime.isoformat(datetime.now())
        self.filename = self.filename[:19]
        self.filename = self.filename.replace(":",".")
        self.filename = self.filename.replace("T","_")
        self.filename = self.filename + ".py"
        self.filename = os.path.join(os.path.dirname(__file__), self.filename)
        self.indent = ""
        print("Compiling program...")
        print(f"Creating file: {self.filename}")

    def write(self, words: str, indent_level: int = 0):
        self.indent = " " * indent_level * 4
        with open(self.filename, "a", encoding="utf8") as nfile:
            nfile.write("\n" + self.indent + words)


def peek(index: int, string: str) -> bool:
    if string[index] == string[-1]:
        return False
    if string[index] == string[index+1]:
        return True
    return False


def execute(code: str):

    nf = NewFile()
    nf.write("from unfuck import Unfuck" + "\n")
    nf.write("f = Unfuck()" + "\n")

    u = Unfuck()

    right_count = 1
    left_count = 1
    add_count = 1
    sub_count = 1
    out_count = 1
    indent = 0

    while u.ip < len(code):
        match code[u.ip]:
            case "+":
                if peek(u.ip, code):
                    add_count += 1
                    u.ip += 1
                    continue

                if add_count != 1:
                    nf.write(f"f.add({add_count})", indent)
                    add_count = 1
                else:
                    nf.write("f.add()", indent)
                u.ip += 1
            case "-":
                if peek(u.ip, code):
                    sub_count += 1
                    u.ip += 1
                    continue

                if sub_count != 1:
                    nf.write(f"f.sub({sub_count})", indent)
                    sub_count = 1
                else:
                    nf.write("f.sub()", indent)
                u.ip += 1
            case ">":
                if peek(u.ip, code):
                    right_count += 1
                    u.ip += 1
                    continue

                if right_count != 1:
                    nf.write(f"f.right({right_count})", indent)
                    right_count = 1
                else:
                    nf.write("f.right()", indent)
                u.ip += 1
            case "<":
                if peek(u.ip, code):
                    left_count += 1
                    u.ip += 1
                    continue

                if left_count != 1:
                    nf.write(f"f.left({left_count})", indent)
                    left_count = 1
                else:
                    nf.write("f.left()", indent)
                u.ip += 1
            case "[":
                nf.write("while f.array[f.dp]:" + "\n", indent)
                indent += 1
                u.ip += 1
            case "]":
                indent -= 1
                u.ip += 1
            case ".":
                if peek(u.ip, code):
                    out_count += 1
                    u.ip += 1
                    continue
                if out_count != 1:
                    nf.write(f"f.out({out_count})", indent)
                    out_count = 1
                else:
                    nf.write("f.out()", indent)
                u.ip += 1
            case ",":
                nf.write("f.input()")
                u.ip += 1


def main():
    if len(sys.argv) != 2:
        exit(f"Usage: '{sys.argv[0]}' filename")

    try:
        with open(sys.argv[1], "r", encoding="utf8") as f:
            file: str = f.read()
            code: str = "".join(c for c in file if c in COMMANDS)
            execute(code)
    except FileNotFoundError:
        exit(f"Error: File '{sys.argv[1]}' not found")


if __name__ == "__main__":
    main()
