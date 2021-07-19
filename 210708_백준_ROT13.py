import string

a = input()

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
ret_string = ""
for char in a:
    if char in alphabet_lower:
        pos = alphabet_lower.find(char)
        char = alphabet_lower[(pos + 13) % len(alphabet_lower)]
    elif char in alphabet_upper:
        pos = alphabet_upper.find(char)
        char = alphabet_upper[(pos + 13) % len(alphabet_upper)]
    ret_string += char

print(ret_string)