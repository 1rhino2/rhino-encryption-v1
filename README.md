# 🦏 rhino-encryption-v1.1

**rhino-encryption-v1.1** is a playful Python tool for scrambling your messages using a custom keyword cipher, digit reversal, hexadecimal encoding, and a final hex digit shift.  
It’s designed for fun, puzzles, and learning—not real security!

---

## ✨ Features

- **Easy to use**: Encrypt messages instantly from CLI or Python.
- **Simple logic, readable code**: Great for learning or demonstrations.
- **Custom keyword masking**: Uses `"RHINO"` as the cipher mask.
- **Extra obfuscation step**: Shifts each hex digit by +1 at the end.
- **Clear test cases**: See [test_cases.txt](test_cases.txt) for examples.

---

## 🔑 How It Works

1. **Alphabet Position**: Each letter becomes its English alphabet number (A=1, ..., Z=26).
2. **Reverse Digits**: If the number is double-digit, reverse the digits (e.g. 12 → 21).
3. **Keyword Mask**: Add the corresponding (cycled) letter from `"RHINO"` to each letter's value (R=18, H=8, I=9, N=14, O=15).
4. **Hexadecimal**: Convert the sum to uppercase hexadecimal.
5. **Hex Digit Shift**: Each hex digit is shifted by +1 (0→1, 1→2, ..., E→F, F→0).
6. **Non-letters**: Spaces become double spaces for clarity; all other characters are preserved.

**Example:**  
"HELLO" → `2B E 2F 34 53`  
See [test_cases.txt](test_cases.txt) for more!

---

## ❓ Is This Secure?

**NO!**  
This is not real encryption—it's just for fun, puzzles, and educational use.  
Anyone with the README or code can easily reverse it.

---

## 🚀 Usage

### Command Line

```bash
python rhino_encryption_v1.py
```
You’ll see:
```
Enter string to encrypt:
```
Type your message and press Enter.

Or, pass your message directly:
```bash
python rhino_encryption_v1.py "HELLO WORLD"
```



---

## 🧪 Example Test Cases

| Input         | Output                              |
|---------------|-------------------------------------|
| HELLO         | 2B E 2F 34 53                       |
| CAB           | 26 A C                              |
| RHINO         | 74 21 23 48 53                      |
| COOL AS HELL! | 26 4C 4D 34   21 7E   21 F 34 35 !  |
| I ❤️ RHINO    | 2C   ❤️   6A 22 18 49 54           |

---

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for full details.

---

## 🛠️ Planned Changes (for v1.2, expected 2025-07-19)

- Make encryption method more secure (e.g. additional obfuscation or mixing steps, optional salt, or stronger keyword mechanics).
- Optional decryption function for v1.1/v1.2 messages.
- Allow user-supplied custom keyword masks via CLI.
- CLI flag for toggling the extra hex digit shift step.
- More test cases and edge case handling.
- Refactor for better modularity and test coverage.

---

## 📁 Files

- `rhino_encryption_v1.py` — the main encryption script
- `test_cases.txt` — test cases and breakdowns
- `README.md` — this file!
- `CHANGELOG.md` — full changelog
- `LICENSE` — MIT license

---

# Also, gl on decrypting since I never rlly made a decryptor.

---

## 📝 License

MIT License.  
Feel free to use, modify, and share—but please keep credit!

Copyright (c) 2025 1rhino2  
See [LICENSE](LICENSE) for full details.
