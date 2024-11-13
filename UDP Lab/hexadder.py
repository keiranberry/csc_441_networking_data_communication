def hex_addition(hex_numbers):
    total = sum(int(num, 16) for num in hex_numbers)
    # Wrap-around carry if the total is larger than 16 bits
    while total > 0xFFFF:
        total = (total & 0xFFFF) + (total >> 16)
    return hex(total)

hex_numbers = """C0A8
0165
4457
47E2 
0011 
0025 
1117 
0035 
0025 
0000 
0004
0100
0001
0000
0000
0000
0377
7777
036d
6974
0365
6475
0000
0100
0100""".splitlines()# Your 16-bit hex numbers
result = hex_addition(hex_numbers)
a = bin(int(result, 16))[2:]
comp = "0b"
for c in a:
    comp += str((1 if c == '0' else 0))

print(len(comp))

print(hex(int(comp, 2)))
