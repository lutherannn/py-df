import ascii
import sys

wordDict = ascii.getCodes()
stack = []
words = list(wordDict.keys())

with open(sys.argv[1], "r") as f:
    input = f.read().splitlines()
    f.close()

for x in input:
    if x in words:
        stack.append(wordDict.get(x))
    else:
        print(f"Input file contains invalid keyword: {x}")
        sys.exit()
with open(sys.argv[2], "w") as f:
    for x in stack:
        f.write(x + "o\n")
    f.close()
