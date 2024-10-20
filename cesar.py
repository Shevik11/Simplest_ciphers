def encrypt_caesar(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # перевіряємо, чи є символ літерою
            shift = key % 33  # враховуємо кількість літер в українському алфавіті
            new_char = chr((ord(char) - ord("А") + shift) % 33 + ord("А"))
            encrypted_text += new_char
        else:
            encrypted_text += char  # залишаємо інші символи без змін
    print(encrypted_text)
    return encrypted_text


def decrypt_caesar(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 33
            new_char = chr((ord(char) - ord("А") - shift) % 33 + ord("А"))
            decrypted_text += new_char
        else:
            decrypted_text += char

    print(decrypted_text)
    return decrypted_text


if __name__ == "__main__":
    # Тестування
    text = "КОТ"
    key = 3
    encrypted = encrypt_caesar(text, key)
    decrypted = decrypt_caesar(encrypted, key)

    print(f"Зашифрований текст: {encrypted}")
    print(f"Розшифрований текст: {decrypted}")
