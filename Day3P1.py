import sys
import string


slope = []
trees = 0

x = 0
y = 0

if len(sys.argv) != 2:
    sys.exit("You forgot the slope!:")

file = open(sys.argv[1], "r")
rawdata = file.readlines()

for lines in rawdata:
    slope.append(lines)

slopewidth = len(slope[0])

file.seek(0, 0)

while x < len(slope):
    if y >= 31:
        y = y - slopewidth + 1
    if slope[x][y] == "#":
        slope[x][y] == "X"
        trees += 1
    else:
        slope[x][y] == "O"
    y += 3
    x += 1







print(trees)


with open('slopeanswer.txt', 'w') as f:
    for lines in slope:
        f.write(lines)

