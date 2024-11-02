def caesar_encrypt(plain_txt: str, skip: int) -> str:
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in plain_txt:
        # for char is 'space'
        if char == " ":
            result += char
            continue

        old_char_idx = alphabets.find(char)
        new_char_idx = (old_char_idx + skip) % 26
        result += alphabets[new_char_idx]

    return result


def caesar_decrypt(encrypted_text: str, skip: int) -> str:
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in encrypted_text:
        if char == " ":
            result += char
            continue

        old_char_idx = alphabets.find(char)
        new_char_idx = old_char_idx - skip
        result += alphabets[new_char_idx]

    return result


def main():
    print("This is Caesar Encryption")
    text_to_encrypt = input("Text to Encrypt : ").upper()
    skip = int(input("Number of letter to skip : "))
    encrypted_text = caesar_encrypt(text_to_encrypt, skip)
    print("The Encrypted Text is...")
    print(encrypted_text)


if __name__ == "__main__":
    main()
