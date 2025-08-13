"""*An example program to test and demonstrate the Unfuck module.*
"""

from unfuck import Unfuck

f = Unfuck()

f.add(12)

while f.array[f.dp]:
    f.right()
    f.add(6)

    f.right()
    f.add(8)

    f.right()
    f.add(9)

    f.right()
    f.add(10)

    f.right()
    f.add(3)

    f.right()
    f.add()

    f.left(6)
    f.sub()

f.right()
f.out()

f.right()
f.add(5)
f.out()

f.right()
f.out(2)

f.add(3)
f.out()

f.right(2)
f.sub(4)
f.out()

f.left()
f.sub()
f.out()

f.left()
f.out()

f.right()
f.sub(5)
f.out()

f.left()
f.sub(3)
f.out()

f.left()
f.sub()
f.out()

f.right(3)
f.add()
f.out()

f.right()
f.sub(2)
f.out()
