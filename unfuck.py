"""*The unfuck module allows you to create Brainfuck programs through Python and higher-level abstraction.*
"""

import sys

class Unfuck:

    def __init__(self):
        self.array = {0: 0}
        self.dp = 0
        self.ip = 0
        self.cell = self.array[self.dp]

    def add(self, num: int = 1):
        self.array[self.dp] = (self.array[self.dp] + num) % 256
        self.cell = self.array[self.dp]

    def sub(self, num: int = 1):
        self.array[self.dp] = (self.array[self.dp] - num) % 256
        self.cell = self.array[self.dp]

    def right(self, dist: int = 1):
        self.dp += dist
        self.array[self.dp] = self.array.setdefault(self.dp, 0)
        self.cell = self.array[self.dp]

    def left(self, dist: int = 1):
        if (self.dp - dist) < 0:
            exit("Pointer moved to nonexistent cell.")
        self.dp -= dist
        self.array[self.dp] = self.array.setdefault(self.dp, 0)
        self.cell = self.array[self.dp]

    def out(self, repeat: int = 1):
        char = chr(self.array[self.dp])
        for i in range(repeat):
            sys.stdout.write(char)

    def input(self):
        self.array[self.dp] = input()
        self.cell = self.array[self.dp]

    # There are no functions for loops.
    # Loops are handled separately through using "while self.cell:"
