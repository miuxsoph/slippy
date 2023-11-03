user_space = input("!:/")
user_slash = input("\\")

I = user_space 
P = user_slash

def convert_string_to_base3(text):
    return int(text.encode('utf-8').hex(), 3)

base3_integer = convert_string_to_base3(user_space)

hex_representation = format(base3_integer, 'X')

print(hex_representation)
hex_input = hex_representation

r = [int(x) for x in format(int(hex_input, 16), '08b')]

def rule30(a, b, c):
    if (a, b, c) in [(0, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0)]:
        return 1
    else:
        return 0

cx, step = 270, 12	
c, cn = [0] * cx, [0] * cx
c[cx // 2:cx // 2 ] = r

for _ in range(step):
    print(''.join([' ' if e == 1 else '!' for e in c[111:162]]))  # Adjust the range here for left alignment
    for i in range(cx):
        x = c[i - 1] if i > 0 else 0
        z = c[i + 1] if i < cx - 1 else 0
        cn[i] = rule30(x, c[i], z)
    c = cn[:]

def slash(I, P):
    while I:
        print(I)
        if I[0] == '/':
            I = I[1:]
        else:
            for c in P:
                if c == "/":
                    I = I[1:]
                elif c == "\\":
                    I = c + I     
                else:
                    break
            if not I:
                break
slash(I, P)
