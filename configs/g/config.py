T = "0xffffffff00000001/"
I = "9/3/1"
P = "/0."
from fractions import Fraction
from time import sleep
import sys

sys.set_int_max_str_digits(640)

ip = Fraction(1, 10000000000000000000000000000001)

commands = [Fraction(3, 2), 10000000000000000000000000000001, 91111111, 0, 3, 11111111111]
user_input = input("Initialize:")

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if is_integer(user_input):
    commands[0] = int(user_input)
else:
    try:
        user_fraction = Fraction(user_input)
        commands[0] = user_fraction
    except ValueError:
        print("Invalid input. Please enter a valid integer or fraction.")

if user_input == '1':
    commands[0] = Fraction(3, 2)
    print("Input changed to 3/2")
elif is_integer(user_input):
    commands[0] = int(user_input)
else:
    try:
        user_fraction = Fraction(user_input)
        commands[0] = user_fraction
    except ValueError:
        print()

denominator = commands[0].denominator

def r30(a, b, c):
    if (a, b, c) in [(0, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0)]:
        return 1
    else:
        return 0

r = [int(x) for x in format(int(input("T:")), '08b')]
cx, step = 180, 26
c, cn = [0] * cx, [0] * cx
c[cx // 2:cx // 2 + 8] = r

for _ in range(step):
    print(''.join(['0' if e == 0 else '1' for e in c[90:123]]))
    for i in range(cx):
        x = c[i - 1] if i > 0 else 0
        z = c[i + 1] if i < cx - 1 else 0
        cn[i] = r30(x, c[i], z)
    c = cn[:]

input_val = None

while ip:
    eip = -ip if input_val else ip
    if eip < 0:
        input_val -= 1
    ci = eip % len(commands)
    if ci < 0:
        ci += len(commands)
    cmd = commands[int(ci)]
    if isinstance(cmd, int):
        print(f"{eip}")
    ip *= Fraction(cmd)
    if isinstance(cmd, Fraction):
        break
    ip *= Fraction(cmd)
    if cmd == 3:
        break

def m(n):
    if n > 100: return n - 10
    return m(m(n + 11))

q, r, w = '100000001', '900001', 3
while q[w:]:
    if r[0] == '0': q = q[1:]
    else:
        r = r[1:] + r[0]
        if q[0] == '1': q += r[0]
    r = r[1:] + r[0]
    q = str(m(int(q)))

    # Convert Base64 to hexadecimal representation
    hex_address = int(q.encode('utf-8').hex(), 36)
    hex_address = "0x{:x}".format(hex_address)
    
    print(hex_address)
