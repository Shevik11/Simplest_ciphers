import tkinter as tk

from atbash import atbash_cipher
from new_window import create_new_window_without_number

shifr_with_num = ['xor', 'cesar']


root = tk.Tk()
root.geometry("400x300")


btn1 = tk.Button(root, text="Атбаш шифрування",
                 command=lambda: create_new_window_without_number(atbash_cipher, atbash_cipher, 'atbash',
                                                                  shifr_with_num, root))
btn1.pack(pady=5)


exitbtn = tk.Button(root, text="Exit", command=root.destroy)
exitbtn.pack(pady=5)

root.mainloop()
