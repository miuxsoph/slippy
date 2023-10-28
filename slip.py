I = "9/3/1"
P = "/0."
from fractions import Fraction
ip = Fraction(1, 1000000000000000000000000000000010000000)
commands = [Fraction(101, 10), 18446744073709551617, 16, 0, 3, 16]
print("IP:", ip)
print("Commands:", [cmd for cmd in commands])

def m(n):
    if n > 100: return n - 10
    return m(m(n + 11))

def rule30(a, b, c):
    if (a, b, c) in [(0, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0)]:
        return 1
    else:
        return 0

r = [int(x) for x in format(int(input("Enter initial state (0-255): ")), '08b')]
cx, step = 180, 26
c, cn = [0] * cx, [0] * cx
c[cx // 2:cx // 2 + 8] = r

for _ in range(step):
    print(''.join(['1' if e == 1 else '0' for e in c[90:130]]))
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

input_val = None
inputdefined = False
output = 1

while ip:
    eip = -ip if input_val else ip
    if eip < 0:
        input_val -= 1
    ci = eip % len(commands)
    if ci < 0:
        ci += len(commands)
    cmd = commands[int(ci)]  # Convert ci to an integer index
    if isinstance(cmd, Fraction):
        print(f"{eip}")
    ip *= Fraction(cmd)

    if cmd == 3:
        break

q, r, w = '100100100100100', '101110101011011101001110101110101110100000', 3
while q[w:]:
    if r[0] == '0': q = q[1:]
    else:
        r = r[1:] + r[0]
        if q[0] == '1': q += r[0]
    r = r[1:] + r[0]
    print(q)
    q = str(m(int(q)))

slash(I, P)
if inputdefined:
    print(output(q))