T = "0xffffffff00000001/"
I = "9/3/1"
P = "/0."
from fractions import Fraction
from math import floor, ceil
from time import sleep
import base64
import sys

# Open a text file to write the output
with open('output.txt', 'w') as text_file:
    # Redirect the standard output to both the console and the text file
    original_stdout = sys.stdout  # Save a reference to the original standard output

    # Define a custom function to write to both the console and the text file
    def write_to_both(*args, **kwargs):
        original_stdout.write(*args, **kwargs)  # Write to the original standard output (console)
        text_file.write(*args, **kwargs)  # Write to the text file

    sys.stdout = write_to_both  # Set the output to write to both console and text file

    # Your entire existing code goes here...

    # Reset the standard output
    sys.stdout = original_stdout

phi = -4122
beta = -8022

fb = lambda x: x * ceil(x/3 - x//3) * ceil(x/5 - x//5) + beta * (1 + floor(x//5 - x/5)) + phi * (1 + floor(x//3 - x//3)) * (1 + (1 + floor(x//5 - x//5)) * 9999)

result_sequence = [fb(i) for i in range(1, 30)]

# Extracting the memory address from the function representation
memory_address = hex(id(fb))

commands = [Fraction(3, 2), 196608, 16, 0, 3, 16]

user_input = input("Initialize:")

# Function to check if the input is an integer
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

Tip = [user_input, 196608, 16, 0, 3, 16]
print(Tip)

def r30(a, b, c):
    if (a, b, c) in [(0, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0)]:
        return 1
    else:
        return 0

def calculate_denominator():
    r = [int(x) for x in format(int(input("T:")), '08b')]
    cx, step = 180, 25
    c, cn = [0] * cx, [0] * cx
    c[cx // 2:cx // 2 + 8] = r

    last_value = None  # To store the last value printed by r30

    for _ in range(step):
        print(''.join(['0' if e == 0 else '1' for e in c[90:123]]))
        for i in range(cx):
            x = c[i - 1] if i > 0 else 0
            z = c[i + 1] if i < cx - 1 else 0
            cn[i] = r30(x, c[i], z)
        c = cn[:]
        last_value = int(''.join(['1' if e == 1 else '0' for e in c[90:122]]))

    return last_value

# Get the last value printed by r30
last_denominator = calculate_denominator()

# Update the Fraction object 'ip' with the last denominator value
ip = Fraction(255, last_denominator + 1)

commands = [Fraction(4, 3), 196608, 16, 0, 3, 16]

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

while ip:
    eip = -ip if input_val else ip
    if eip < 0:
        input_val -= 1
    ci = eip % len(commands)
    if ci < 0:
        ci += len(commands)
    cmd = commands[int(ci)]
    if isinstance(cmd, int):
        print(f"{cmd}")
        sleep(0.02)
    ip *= Fraction(cmd)

    if cmd == 3:
        break

def m(n):
    if n > 100:
        return n - 10
    return m(m(n + 11))

initial_hex_value = "100100100100100"  # Initial hex value for conversion to binary
q, r, w = bin(int(initial_hex_value, 16))[2:], '101110101011011101001110101110101110100000', 3

multiplier = 0xffffffff00000001

def fizz_buzz(n):
    result = []
    for num in result_sequence:  # Change 'sequence' to 'result_sequence'
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result

S = fb(30)

# Convert hexadecimal string to an integer
numeric_memory_address = Fraction(1, S)

fizz_buzz_output = fizz_buzz(result_sequence)

def AuxM(binary_value):
    decimal_value = int(binary_value, 2)  # Convert binary to decimal
    result = m(decimal_value)  # Use the existing 'm' function on the decimal value
    return bin(result)[2:]  # Convert the result back to binary and remove the '0b' prefix


unique_hex_addresses = set()  # Store unique hex addresses

while q[w:]:
    if r[0] == '0':
        q = q[1:]
    else:
        r = r[1:] + r[0]
        if q[0] == '1':
            q += r[0]
        r = r[1:] + r[0]  # Indent this line to match with the 'else' block
        if q[0] == '1':  # Add necessary indentation for the subsequent lines
            q += r[0]
    r = r[1:] + r[0]

    encoded_q = base64.b64encode(q.encode()).decode()
    hex_address = int(encoded_q.encode('utf-8').hex(), 36)
    hex_address = "0x{:X}".format(hex_address)

    # Check if the current hex address is in the set of unique addresses
    if hex_address not in unique_hex_addresses:
        print(hex_address)
        unique_hex_addresses.add(hex_address)
    else:
        binary_last_value = bin(int(hex_address, 36))[2:]
        r = AuxM(binary_last_value)

        while q[w:]:
            if r[0] == '0':
                q = q[1:]
            else:
                r = r[1:] + r[0]
                if q[0] == '1':
                    q += r[0]
                r = r[1:] + r[0]
                if q[0] == '1':
                    q += r[0]
            r = r[1:] + r[0]
            encoded_q = base64.b64encode(q.encode()).decode()
            hex_address = int(encoded_q.encode('utf-8').hex(), 36)
            hex_address = "0x{:X}".format(hex_address)
            print(hex_address)
print(memory_address)            
