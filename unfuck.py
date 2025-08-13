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
        """*Adds a whole number to the pointed cell*.
        *If the pointed cell has a value of 255, the value will go to 0*.

        Args:
            num (int, optional): *Addend*. Defaults to 1.
        """
        self.array[self.dp] = (self.array[self.dp] + num) % 256
        self.cell = self.array[self.dp]

    def sub(self, num: int = 1):
        """*Subtracts a whole number from the pointed cell*.
        *If the pointed cell has a value of 0, the value will go to 255*.

        Args:
            num (int, optional): *Subtrahend*. Defaults to 1.
        """
        self.array[self.dp] = (self.array[self.dp] - num) % 256
        self.cell = self.array[self.dp]

    def right(self, dist: int = 1):
        """*Moves the data pointer to the right by a whole number*.

        Args:
            dist (int, optional): *Distance to the right*. Defaults to 1.
        """
        self.dp += dist
        self.array[self.dp] = self.array.setdefault(self.dp, 0)
        self.cell = self.array[self.dp]

    def left(self, dist: int = 1):
        """*Moves the data pointer to the left by a whole number*.
        *Data pointer cannot move further left than 0.*

        Args:
            dist (int, optional): *Distance to the left*. Defaults to 1.
        """
        if (self.dp - dist) < 0:
            exit("Pointer moved to nonexistent cell.")
        self.dp -= dist
        self.array[self.dp] = self.array.setdefault(self.dp, 0)
        self.cell = self.array[self.dp]

    def out(self, repeat: int = 1):
        """*Outputs the pointed cell's value in ASCII*.

        Args:
            repeat (int, optional): *Amount of outputs*. Defaults to 1.
        """
        char = chr(self.array[self.dp])
        for i in range(repeat):
            sys.stdout.write(char)

    def input(self):
        """*Takes a character input and sets the pointed cell to the corresponding ASCII value.*.
        """
        self.array[self.dp] = input()
        self.cell = self.array[self.dp]

    # There are no functions for loops.
    # Loops are handled separately through using "while self.cell:"

    def goto(self, index: int = 0):
        """*Moves pointer to the indicated cell*.

        Args:
            index (int, optional): *Cell number*. Defaults to 0.
        """
        self.dp = index
        self.cell = self.array[self.dp]

    def debug(self):
        """*Shows current values of all existing cells and where the data pointer is*.
        """
        for i in enumerate(self.array):
            if i != self.dp:
                print(f"[{i}: {self.array[i]}]")
            else:
                print(f">>> [{i}:{self.array[i]}]")
