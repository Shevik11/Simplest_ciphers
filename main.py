import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk

from atbash import atbash_cipher
from new_window import create_new_window_without_number
from xor import xor
from cesar import encrypt_caesar, decrypt_caesar
from vigenere import encrypt, decrypt
from sparta import sparta_encrypt, sparta_decrypt
from polibiy import polibius_encrypt, polybius_decrypt

DEFAULT_ALPHABET_UA = (
    "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
)
DEFAULT_ALPHABET_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def make_textmenu(root):
    global the_menu
    the_menu = tk.Menu(root, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")
    the_menu.add_separator()
    the_menu.add_command(label="Select all")


def callback_select_all(event):
    root.after(50, lambda: event.widget.select_range(0, "end"))


def show_textmenu(event):
    e_widget = event.widget
    try:
        the_menu.entryconfigure(
            "Cut", command=lambda: e_widget.event_generate("<<Cut>>")
        )
        the_menu.entryconfigure(
            "Copy", command=lambda: e_widget.event_generate("<<Copy>>")
        )
        the_menu.entryconfigure(
            "Paste", command=lambda: e_widget.event_generate("<<Paste>>")
        )
        the_menu.entryconfigure(
            "Select all", command=lambda: e_widget.select_range(0, "end")
        )
        the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)
    except Exception as e:
        print(f"Помилка при показі контекстного меню: {e}")


def load_and_resize_icon(path, size=(20, 20)):
    try:
        image = Image.open(path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Помилка завантаження іконки {path}: {e}")
        return None


shifr_with_num = ["xor", "cesar", "vigenere", "sparta", "polibiy"]

root = tk.Tk()
root.geometry("400x500")
root.title("Методи шифрування")
root.configure(bg="#f0f0f0")

# Створюємо головний фрейм
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Заголовок
title_label = ttk.Label(
    main_frame, text="Методи шифрування", font=("Helvetica", 16, "bold")
)
title_label.pack(pady=20)

# Словник з іконками та функціями шифрування
encryption_functions = {
    "Атбаш шифрування": {
        "icon": "photo/atbash.png",
        "command": lambda: create_new_window_without_number(
            atbash_cipher, atbash_cipher, "atbash", shifr_with_num, root
        ),
    },
    "Шифрування XOR": {
        "icon": "photo/xor.png",
        "command": lambda: create_new_window_without_number(
            xor, xor, "xor", shifr_with_num, root
        ),
    },
    "Шифрування Цезаря": {
        "icon": "photo/cesar.png",
        "command": lambda: create_new_window_without_number(
            lambda text, key: encrypt_caesar(text, key),
            lambda text, key: decrypt_caesar(text, key),
            "cesar",
            shifr_with_num,
            root,
        ),
    },
    "Шифрування Віженера": {
        "icon": "photo/vigenere.png",
        "command": lambda: create_new_window_without_number(
            lambda text, key: encrypt(
                text,
                key,
                (
                    DEFAULT_ALPHABET_UA
                    if any(c in DEFAULT_ALPHABET_UA for c in text)
                    else DEFAULT_ALPHABET_EN
                ),
            ),
            lambda text, key: decrypt(
                text,
                key,
                (
                    DEFAULT_ALPHABET_UA
                    if any(c in DEFAULT_ALPHABET_UA for c in text)
                    else DEFAULT_ALPHABET_EN
                ),
            ),
            "vigenere",
            shifr_with_num,
            root,
        ),
    },
    "Шифр Давньої Спарти Скитала": {
        "icon": "photo/sparta.png",
        "command": lambda: create_new_window_without_number(
            lambda text, key: sparta_encrypt(text, key),
            lambda text, key: sparta_decrypt(text, key),
            "sparta",
            shifr_with_num,
            root,
        ),
    },
    "Квадрат Полібія": {
        "icon": "photo/polibiy.png",
        "command": lambda: create_new_window_without_number(
            lambda text, key: polibius_encrypt(text, key),
            lambda text, key: polybius_decrypt(text, key),
            "polibiy",
            shifr_with_num,
            root,
        ),
    },
}

# Створення стилю для кнопок
style = ttk.Style()
style.configure("Custom.TButton", padding=(10, 5, 10, 5))

# Створення кнопок з іконками
for text, data in encryption_functions.items():
    # Створюємо фрейм для кнопки
    btn_frame = ttk.Frame(main_frame)
    btn_frame.pack(pady=8, padx=20, fill=tk.X)

    # Завантажуємо іконку
    icon = load_and_resize_icon(data["icon"])

    # Створюємо кнопку
    btn = ttk.Button(
        btn_frame,
        text=text,
        command=data["command"],
        style="Custom.TButton",
        cursor="hand2",
    )
    btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # Якщо іконка успішно завантажена, додаємо її до кнопки
    if icon:
        btn.image = icon  # Зберігаємо посилання на зображення
        btn.configure(image=icon, compound=tk.LEFT)

# Кнопка виходу з іконкою
exit_icon = load_and_resize_icon("photo/exit.png")
exit_btn = ttk.Button(
    main_frame, text="Вихід", command=root.quit, style="Custom.TButton", cursor="hand2"
)

if exit_icon:
    exit_btn.image = exit_icon
    exit_btn.configure(image=exit_icon, compound=tk.LEFT)

exit_btn.pack(pady=(20, 0), padx=20, fill=tk.X)

# Інформаційний текст
info_label = ttk.Label(
    main_frame, text="© 2024 Encryption Tools", font=("Helvetica", 8)
)
info_label.pack(side=tk.BOTTOM, pady=10)

# Контекстне меню для тексту
make_textmenu(root)
root.bind_class("Text", "<Button-3><ButtonRelease-3>", show_textmenu)
root.bind_class("Text", "<Control-a>", callback_select_all)

root.mainloop()
