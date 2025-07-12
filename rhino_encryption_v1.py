import sys

def rhino_encrypt(text, mask_keyword="RHINO"):
    """
    Encrypt a string using Rhino Encryption V1.
    Steps:
    1. Map each letter to its alphabetical position (A=1, ..., Z=26).
    2. Reverse the digits of the number.
    3. Add the alphabetical position of the corresponding letter in the mask_keyword (cycling through).
    4. Convert the result to uppercase hexadecimal.
    Non-letter characters are preserved. Double space between words.
    """
    mask = [ord(c.upper()) - ord('A') + 1 for c in mask_keyword]
    mask_len = len(mask)
    output = []
    mask_idx = 0

    for char in text:
        if char.isalpha():
            pos = ord(char.upper()) - ord('A') + 1
            rev = int(str(pos)[::-1])
            masked = rev + mask[mask_idx % mask_len]
            hexed = format(masked, 'X').upper()
            output.append(hexed)
            mask_idx += 1
        elif char == " ":
            output.append("  ")  # Double space between words
        else:
            output.append(char)
    return ' '.join(output).replace("    ", "   ")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    else:
        message = input("Enter string to encrypt:\n")
    print(rhino_encrypt(message))
