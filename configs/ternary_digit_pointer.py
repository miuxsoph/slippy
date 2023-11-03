T = " !"
I = "9/3/1"
P = "/0."

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

slash(I, P)
