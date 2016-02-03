"""
multiplication-table.py
Author: Daniel Wilson
Credit: <list sources used, if any>
Assignment:

Write and submit a Python program that prints a multiplication table. The user 
must be able to determine the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
wq = int(float(input("What is the width of the multiplication table? ")))
hq = int(float(input("What is the height of the multiplicaton table? ")))

for x in range(1, wq) :
    for y in range(2, hq) :
        print("X", "x")



