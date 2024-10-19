special_character = [' ', ',', '.', '!', '?', ':', ';', '(', ')', '-', '_', '+', '=', '*', '/', '\\', '|', '[', ']', '{', '}', '<', '>', '@', '#', '$', '%', '^', '&', '~', '`', '"', "'"]
def atbash_cipher(text):
    if not text:
        raise ValueError("Input text cannot be empty")

    ukr_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    lat_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ukr_reversed = ukr_alphabet[::-1]
    lat_reversed = lat_alphabet[::-1]

    result = []
    for char in text:
        if char.upper() in ukr_alphabet:
            index = ukr_alphabet.index(char.upper())
            result.append(ukr_reversed[index] if char.isupper() else ukr_reversed[index].lower())
        elif char.upper() in lat_alphabet:
            index = lat_alphabet.index(char.upper())
            result.append(lat_reversed[index] if char.isupper() else lat_reversed[index].lower())
        elif char in special_character:
            result.append(char)
        else:
            raise ValueError(f"Invalid character found: {char}")
    print(''.join(result))
    return ''.join(result)


if __name__ == "__main__":
    # Example usage
    try:
        encrypted_text = atbash_cipher("Привіт World")
        print(encrypted_text)
    except ValueError as e:
        print(e)