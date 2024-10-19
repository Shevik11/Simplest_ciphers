import tkinter as tk

from atbash import atbash_cipher
from new_window import create_new_window_without_number
from xor import xor



def make_textmenu(root):
    global the_menu
    the_menu = tk.Menu(root, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")
    the_menu.add_separator()
    the_menu.add_command(label="Select all")


def callback_select_all(event):
    # select text after 50ms
    root.after(50, lambda: event.widget.select_range(0, 'end'))


def show_textmenu(event):
    e_widget = event.widget
    try:
        the_menu.entryconfigure("Cut", command=lambda: e_widget.event_generate("<<Cut>>"))
        the_menu.entryconfigure("Copy", command=lambda: e_widget.event_generate("<<Copy>>"))
        the_menu.entryconfigure("Paste", command=lambda: e_widget.event_generate("<<Paste>>"))
        the_menu.entryconfigure("Select all", command=lambda: e_widget.select_range(0, 'end'))
        the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)
    except Exception as e:
        print(f"Помилка при показі контекстного меню: {e}")


shifr_with_num = ['xor', 'cesar']


root = tk.Tk()
root.geometry("400x300")

# bind the feature to all Entry widget
root.bind_class("Text", "<Button-3><ButtonRelease-3>", show_textmenu)
root.bind_class("Text", "<Control-a>", callback_select_all)

btn1 = tk.Button(root, text="Атбаш шифрування",
                 command=lambda: create_new_window_without_number(atbash_cipher, atbash_cipher, 'atbash',
                                                                  shifr_with_num, root))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Шифрування XOR",
                 command=lambda: create_new_window_without_number(xor, xor, 'xor', shifr_with_num, root))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Шифрування Цезаря",
                 command=lambda: create_new_window_without_number(None, None, 'ceasar'))
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Шифрування Віженера",
                 command=lambda: create_new_window_without_number(None, None, 'vigenere'))
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Шифр давньої Спарти Скитала",
                 command=lambda: create_new_window_without_number(None, None, 'scytale'))
btn5.pack(pady=5)

btn6 = tk.Button(root, text="Квадрат Полібія", command=lambda: create_new_window_without_number(None, None, 'polybius'))
btn6.pack(pady=5)

exitbtn = tk.Button(root, text="Вихід", command=root.destroy)
exitbtn.pack(pady=5)

root.mainloop()
