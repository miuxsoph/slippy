# Start File



# Section 1: Imports and about

import warnings
import sys

__about__ = {
"name": "􏿾",
"long_name": "soh supplementary private use area-b u+10fffe",
"function_name": "soh_supplementary_private_use_area_b_u_plus_10fffe",
"file_name": "soh_supplementary_private_use_area_b_u_plus_10fffe.py",
"base_error_name": "SOH10FFFE_error",
"base_warning_name": "SOH10FFFE_warning",
"file_extension": ".soh10fffe",
}

# End Section


# Section 2: Helper functions

def bin_list(text: str, encoding: str = "utf-8") -> list[int]:
    """Takes a string and converts it into a list of bits using the specified encoding, defaulting to utf-8."""
    bin_nums_8 = [*map(lambda x:bin(x)[2:].rjust(8, '0'), text.encode(encoding))]
    output = []
    for string in bin_nums_8:
        output.extend(string)
    return [*map(int, output)]

def bin_to_text(binary_list: list[int], encoding: str = "utf-8") -> str:
    """Takes a list of bits and converts it into a string using the specified encoding, defaulting to utf-8."""
    if len(binary_list) % 8:
        warnings.warn(OutputBitBufferWarning("nice"))
    base_256 = []
    temp = []
    for bit in binary_list:
        temp.append(str(bit))
        if len(temp) == 8:
            base_256.append(int(''.join(temp), 2))
            temp = []
    try:
        return bytes(base_256).decode(encoding)
    except UnicodeDecodeError:
        raise CharError("Unable to decode bytes") from None

# End section


# Section 3: Compiler

def soh_supplementary_private_use_area_b_u_plus_10fffe(code: str) -> str:
    """Runs a program in the 􏿾 language and returns the output."""
    tape_length = 50000
    output = ""
    output_bit_buffer = []
    bit_tape = [0] * tape_length
    pointer = 0
    current_char = 0
    while current_char < len(code):
        match code[current_char]:
            case "": # We take input
                print("Program is requesting user input:")
                bit_input = bin_list(sys.stdin.read(), "utf-8" if bit_tape[pointer] else "latin-1")
                bit_tape[pointer : pointer + len(bit_input)] = bit_input
            case "􏿾": # We print the output bit buffer
                output += bin_to_text(output_bit_buffer, "utf-8" if bit_tape[pointer] else "latin-1")
            case "1": # We place a bit into the output bit buffer
                output_bit_buffer.append(bit_tape[pointer])
            case "0": # We pop a bit from the output bit buffer and overwrite the current bit with it
                bit_tape[pointer] = output_bit_buffer.pop()
            case ">": # The cursor moves right
                pointer += 1
                pointer %= tape_length
            case "<": # The cursor moves left
                pointer -= 1
                pointer %= tape_length
            case "-": # We invert the current bit
                bit_tape[pointer] = (bit_tape[pointer] + 1) % 2
            case "?": # We skip the next element if the current bit is 1
                if bit_tape[pointer]:
                    current_char += 1
            case "A": # Binary AND
                bit_tape[pointer] = +(bit_tape[(pointer-1) % tape_length] and bit_tape[(pointer-2) % tape_length])
            case "O": # Binary OR
                bit_tape[pointer] = +(bit_tape[(pointer-1) % tape_length] or bit_tape[(pointer-2) % tape_length])
            case "N": # Binary NAND
                bit_tape[pointer] = +(not (bit_tape[(pointer-1) % tape_length] and bit_tape[(pointer-2) % tape_length]))
            case "X": # Binary XOR
                bit_tape[pointer] = +((bit_tape[(pointer-1) % tape_length] or bit_tape[(pointer-2) % tape_length]) and not (bit_tape[(pointer-1) % tape_length] and bit_tape[(pointer-2) % tape_length]))
            case "|": # Go back to the beginning
                current_char = -1
            case _: # We do nothing
                pass
        current_char += 1
    return output

# End Section


# Section 4: Error Classes

class SOH10FFFE_error(RuntimeError):
    """Base exception for 􏿾 programs."""

class SOH10FFFE_warning(SOH10FFFE_error):
    """Base warning for 􏿾 programs."""

class OutputBitBufferWarning(SOH10FFFE_warning):
    """There may be unexpected behaviour with the output bit buffer."""

class CharError(SOH10FFFE_error, UnicodeError):
    """Something wrong with encoding/decoding in the program."""

# End Section


# Section 5: Main

if __name__ == "__main__":
    run_code = False
    try:
        if sys.argv[1] == "-c":
            run_code = True
    except IndexError:
        pass

    if run_code:
        code = input("Enter code: ")
    else:
        with open(input("Enter filepath: "), encoding="utf-8") as f:
            code = f.read()
    print(soh_supplementary_private_use_area_b_u_plus_10fffe(code))
        

# End Section



# End File