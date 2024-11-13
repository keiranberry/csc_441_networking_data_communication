# data = """
# c0a8
# 0165
# 4457
# 47e2
# 0011
# 1117
# 0035

# 0025

# 0000

# 0004
# 0100
# 0001
# 0000
# 0000
# 0000
# 0377
# 7777
# 036d
# 6974
# 0365
# 6475
# 0000
# 0100
# 0100"""

data = """C0A8
0165
4457
47E2 
0011 
0025 
1117 
0035 
0025 
0000 
0000 
0401 
0000 
0100 
0000 
0000 
0003 
7777 
7703 
6D69 
7403 
6564 
7500 
0001 
0001"""

total = 0

for row in data.splitlines():
    if row == "":
        continue
    val = int(row, 16)

    total += val

    strHex = str(hex(total))[2:]

    if len(strHex) == 5:
        total = int(strHex[1:], 16) + int(strHex[0], 16)

print(strHex.upper())
a = bin(int(strHex, 16))[2:]
comp = "0b"
for c in a:
    comp += str((1 if c == '0' else 0))

print(len(comp))

print(hex(int(comp, 2)))