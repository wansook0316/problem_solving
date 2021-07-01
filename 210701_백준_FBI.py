import re
import sys

input = sys.stdin.readline

fbi = []
p = re.compile("FBI")
for i in range(5):
    if p.search(input()) != None:
        fbi.append(i + 1)
fbi.sort()
if not fbi:
    print("HE GOT AWAY!")
else:
    print(" ".join(list(map(str, fbi))))

# N-FBI1
# 9A-USKOK
# I-NTERPOL
# G-MI6
# RF-KGB1