def sparta_encrypt(text, d):
    k = len(text) % d
    if k > 0:
        # доповнюємо рядок пробілами
        text += ' ' * (d - k)

    column = len(text) // d
    result = ""

    for i in range(column):
        for j in range(d):
            result += text[i + column * j]

    return result


def sparta_decrypt(text, d):
    column = len(text) // d
    symbols = [''] * len(text)
    index = 0
    for i in range(column):
        for j in range(d):
            symbols[i + column * j] = text[index]
            index += 1

    return ''.join(symbols)


if __name__ == "__main__":
    message = input("Введіть текст повідомлення: ")
    diameter = int(input("Введіть діаметр циліндра: "))
    enc_text = sparta_encrypt(message, diameter)
    print("Зашифрований текст: {}".format(enc_text))
    print("Розшифрований текст: {}".format(sparta_decrypt(enc_text, diameter)))