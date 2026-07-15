def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text


print("=" * 45)
print("   Basic Encryption & Decryption")
print("        Caesar Cipher")
print("=" * 45)

message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\n----------- OUTPUT -----------")
print("Original Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
print("------------------------------")