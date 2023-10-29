T = "0xffffffff00000001/"
I = "9/3/1"
P = "/0."
from fractions import Fraction
ip = Fraction(1, 100100100100100)
commands = [Fraction(3, 2), 18446744073709551617, 16, 0, 3, 16]
print("IP:", ip)
print("C:", [cmd for cmd in commands])

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

def print_bcd(text):
    bcd_text = ""
    for character in text:
        ascii_value = ord(character)
        high_nibble = ascii_value // 10
        low_nibble = ascii_value % 10
        bcd_text += f"{high_nibble}{low_nibble}"
    print(bcd_text)

# Function to convert strings to base-3 integers
def convert_string_to_base3(text):
    return int(text.encode('utf-8').hex(), 3)

user_space = input("!:/")
user_slash = input("\\")

I = user_space  # Assign the user input to variable I
P = user_slash

if I[0] == ' ':
    I = I[1:]
else:
    for c in I:
        if c == " ":
            I = I[1:]
        elif c == "\\":
            I = c + I
        else:
            break

if not I:
    print(" ")
else:
    print(I)

base3_integer = convert_string_to_base3(user_space)

hex_representation = format(base3_integer, 'X')

print(hex_representation)
hex_input = hex_representation

# Convert the hexadecimal string to an integer and generate the list 'r'
r = [int(x) for x in format(int(hex_input, 16), '08b')]

def rule30(a, b, c):
    if (a, b, c) in [(0, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0)]:
        return 1
    else:
        return 0

cx, step = 180, 28	
c, cn = [0] * cx, [0] * cx
c[cx // 2:cx // 2 ] = r

for _ in range(step):
    print(''.join(['1' if e == 1 else '0' for e in c[100:130]]))  # Adjust the range here for left alignment
    for i in range(cx):
        x = c[i - 1] if i > 0 else 0
        z = c[i + 1] if i < cx - 1 else 0
        cn[i] = rule30(x, c[i], z)
    c = cn[:]

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
        print(f"{eip}:{cmd}:")
    if isinstance(cmd, int):
        print(f"{eip}:{cmd}:")
    ip *= Fraction(cmd)

    if cmd == 3:
        break

def m(n):
    if n > 100: return n - 10
    return m(m(n + 11))

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
