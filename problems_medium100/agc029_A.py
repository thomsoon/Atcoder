import io
import sys
_INPUT = """\
BWBWBW
"""
sys.stdin = io.StringIO(_INPUT)

S = input()

count = 0
b = 0
for i, c in enumerate(S):
    if c == "W":
        count += b
    else:
        b +=1
print(count)