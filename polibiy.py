import math

DEFAULT_ALPHABET_UA = (
    "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
)
DEFAULT_ALPHABET_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def get_square(key, alphabet):
    new_alphabet = alphabet
    for char in key:
        new_alphabet = new_alphabet.replace(char, "")

    new_alphabet = key + new_alphabet + "0123456789!@#$%^&*)_+-=<>?,."
    n = math.ceil(math.sqrt(len(alphabet)))
    square = [["" for _ in range(n)] for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if index < len(new_alphabet):
                square[i][j] = new_alphabet[index]
                index += 1
    return square


def find_symbol(symbols_table, symbol):
    for i, row in enumerate(symbols_table):
        for j, char in enumerate(row):
            if char == symbol:
                return j, i
    return -1, -1


def polibius_encrypt(text, password, method="Method1", alphabet=DEFAULT_ALPHABET_EN):
    output_text = ""
    square = get_square(password, alphabet)
    if method == "Method1":
        for char in text:
            col, row = find_symbol(square, char)
            if col != -1 and row != -1:
                new_row = 0 if row == len(square) - 1 else row + 1
                output_text += square[new_row][col]
    elif method == "Method2":
        coordinates = []
        for char in text:
            col, row = find_symbol(square, char)
            if col != -1 and row != -1:
                coordinates.append((col, row))
        for col, row in coordinates:
            output_text += square[row][col]
    return output_text


def polybius_decrypt(text, password, method="Method1", alphabet=DEFAULT_ALPHABET_EN):
    output_text = ""
    square = get_square(password, alphabet)
    if method == "Method1":
        for char in text:
            col, row = find_symbol(square, char)
            if col != -1 and row != -1:
                new_row = len(square) - 1 if row == 0 else row - 1
                output_text += square[new_row][col]
    elif method == "Method2":
        coordinates = []
        for char in text:
            col, row = find_symbol(square, char)
            if col != -1 and row != -1:
                coordinates.append((col, row))
        for col, row in coordinates:
            output_text += square[row][col]
    return output_text


if __name__ == "__main__":
    message = input("Введіть текст: ").upper()
    password = input("Введіть пароль(без повторення символів): ").upper()
    alphabet = (
        DEFAULT_ALPHABET_UA
        if any(c in DEFAULT_ALPHABET_UA for c in message)
        else DEFAULT_ALPHABET_EN
    )
    cipher_text = polibius_encrypt(message, password, alphabet=alphabet)
    print(f"Зашифрований текст: {cipher_text}")
    decrypted_text = polybius_decrypt(cipher_text, password, alphabet=alphabet)
    print(f"Розшифрований текст: {decrypted_text}")
