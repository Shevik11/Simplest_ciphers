def get_repeat_key(s, n):
    p = s
    while len(p) < n:
        p += p
    return p[:n]


def vigenere(text, password, alphabet, encrypting=True):
    gamma = get_repeat_key(password, len(text))
    ret_value = ""
    q = len(alphabet)

    for i in range(len(text)):
        letter_index = alphabet.find(text[i])
        code_index = alphabet.find(gamma[i])
        if letter_index < 0:
            ret_value += text[i]
        else:
            ret_value += alphabet[
                (q + letter_index + (1 if encrypting else -1) * code_index) % q
            ]

    return ret_value


def encrypt(plain_message, password, alphabet):
    return vigenere(plain_message, password, alphabet)


def decrypt(encrypted_message, password, alphabet):
    return vigenere(encrypted_message, password, alphabet, encrypting=False)


if __name__ == "__main__":
    alphabet_ua = DEFAULT_ALPHABET_UA
    alphabet_en = DEFAULT_ALPHABET_EN
    input_text = input("Введіть текст: ")
    password = input("Введіть ключ: ")
    alphabet = alphabet_ua if any(c in alphabet_ua for c in input_text) else alphabet_en
    encrypted_text = encrypt(input_text, password, alphabet)
    print(f"Зашифроване повідомлення: {encrypted_text}")
    print(f"Розшифроване повідомлення: {decrypt(encrypted_text, password, alphabet)}")
