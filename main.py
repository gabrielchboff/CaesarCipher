from Cipher import CaesarCipher


def main():
    print("Welcome to Caesar Cipher")
    text = input("Enter text: ")
    key = int(input("Enter key: "))

    cipher = CaesarCipher(text, key)
    print("Encrypted text: " + cipher.encrypt())

    opt = input("Do you want to decrypt? (y/n): ")
    if opt == "y":
        print("Decrypted text: " + cipher.decrypt())
    else:
        print("Goodbye")
        exit(0)

if __name__ == "__main__":
    main()