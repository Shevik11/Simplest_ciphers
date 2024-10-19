def xor_cipher(text, key):
    key_length = len(key)
    encrypted_text = "".join(chr(ord(char) ^ ord(key[i % key_length])) for i, char in enumerate(text))
    return encrypted_text


def xor():
    try:
        type_of_input = input("Input type text(t) or file(f): ").strip()
        if type_of_input not in ["t", "f"]:
            print("Unknown input type, write t or f.")
            return

        if type_of_input == "t":
            action = input("Write action: S or D: ").strip()
            text = input("Write your text: ").strip()
            key = input("Write key: ").strip()
            print(xor_cipher(text, key))

        else:
            action = input("Write action: S or D: ").strip()
            if action not in ["S", "D"]:
                print("Unknown action, write S or D.")
                return

            input_file = input("Write address to input file: ").strip()
            output_file = input("Write address to output file: ").strip()
            key = input("Write key: ").strip()

            try:
                with open(input_file, "r", encoding="utf-8") as f:
                    text = f.read()
            except FileNotFoundError:
                print(f"404 File {input_file} not found.")
                return
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
                return

            result_text = xor_cipher(text, key)

            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(result_text)
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")
                return

            print(f"Result was written in {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    xor()