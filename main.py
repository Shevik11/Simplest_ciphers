import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

exitbtn = tk.Button(root, text="Exit", command=root.destroy)
exitbtn.pack(pady=5)

root.mainloop()
