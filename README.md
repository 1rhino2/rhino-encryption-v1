# 🦏 rhino-encryption-v1

**rhino-encryption-v1** is a playful Python tool for scrambling your messages using a custom keyword cipher, digit reversal, and hexadecimal encoding.  
It’s designed for fun, puzzles, and learning—not real security!

---

## ✨ Features

- **Easy to use**: Encrypt messages instantly from CLI or Python.
- **Simple logic, readable code**: Great for learning or demonstrations.
- **Custom keyword masking**: Uses `"RHINO"` as the cipher mask.
- **Clear test cases**: See [test_cases.txt](test_cases.txt) for examples.

---

## 🔑 How It Works

1. **Alphabet Position**: Each letter becomes its English alphabet number (A=1, ..., Z=26).
2. **Reverse Digits**: If the number is double-digit, reverse the digits (e.g. 12 → 21).
3. **Keyword Mask**: Add the corresponding (cycled) letter from `"RHINO"` to each letter's value (R=18, H=8, I=9, N=14, O=15).
4. **Hexadecimal**: Convert the sum to uppercase hexadecimal.
5. **Non-letters**: Spaces become double spaces for clarity; all other characters are preserved.

**Example:**  
"HELLO" → `1A D 1E 23 42`  
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

### As a Python Module

```python
from rhino_encryption_v1 import rhino_encrypt
print(rhino_encrypt("RHINO"))  # Output: 63 10 12 37 42
```

---

## 🧪 Example Test Cases

| Input         | Output                              |
|---------------|-------------------------------------|
| HELLO         | 1A D 1E 23 42                       |
| CAB           | 15 9 B                              |
| RHINO         | 63 10 12 37 42                      |
| COOL AS HELL! | 15 3B 3C 23   10 6D   10 E 23 24 !  |
| I ❤️ RHINO    | 1B   ❤️   59 11 17 38 45           |

---

## 📁 Files

- `rhino_encryption_v1.py` — the main encryption script
- `test_cases.txt` — test cases and breakdowns
- `README.md` — this file!
- `LICENSE` — MIT license

---

# Also, gl on decrypting since I never rlly made a decryptor.
---

## 📝 License

MIT License.  
Feel free to use, modify, and share—but please keep credit!

Copyright (c) 2025 1rhino2  
See [LICENSE](LICENSE) for full details.
