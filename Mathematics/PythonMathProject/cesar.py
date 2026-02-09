def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ===== SIMPLE APP =====
print("=== Caesar Cipher ===")
choice = input("Upiši (e) za šifriranje ili (d) za dešifriranje: ").lower()

text = input("Upiši tekst: ")
shift = int(input("Upiši pomak (npr. 3): "))

if choice == "e":
    print("\nŠifrirani tekst:")
    print(caesar_encrypt(text, shift))
elif choice == "d":
    print("\nDešifrirani tekst:")
    print(caesar_decrypt(text, shift))
else:
    print("Pogrešan izbor!")
