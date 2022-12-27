# There's literally no reason this should exist. Nobody will use it.
# This is my cry for help.


import sys
import ascii

counter = 0
output = []
keywords = ascii.getCodes()

with open(sys.argv[1]) as f:
    for line in f:
        if line[0] == "#":
            line = ""
        for x in line:
            if x == "i":
                counter += 1
            if x == "d":
                counter -= 1
            if x == "s":
                counter = counter**2
            if x == "o":
                output.append(counter)
                counter = 0

for x in output:
    print(chr(x), end="")
