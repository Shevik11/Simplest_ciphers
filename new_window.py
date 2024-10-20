import tkinter as tk
from tkinter import filedialog


def open_file(text_field):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text_field.delete("1.0", tk.END)
            text_field.insert(tk.END, file.read())


def create_new_window_without_number(
    first_command, second_command, shifr, shifr_with_num, root
):
    new_window = tk.Toplevel(root)
    new_window.geometry("500x500")

    text_field = tk.Text(new_window, height=5, width=30)
    text_field.pack(pady=10)

    result_text = tk.Text(new_window, height=5, width=30)
    result_text.pack(pady=10)

    def execute_command(command):
        if command:
            try:
                if shifr == 'vigenere':
                    key = str(shift.get())
                    result = command(text_field.get("1.0", tk.END).strip(), key)
                elif shifr in shifr_with_num:  # Перевірка чи потрібен ключ
                    key = int(shift.get())
                    result = command(text_field.get("1.0", tk.END).strip(), key)
                else:
                    result = command(text_field.get("1.0", tk.END).strip())

                result_text.delete("1.0", tk.END)  # Очистити текстове поле результату
                result_text.insert(tk.END, result)  # Вставити результат
            except ValueError as e:
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, str(e))
        else:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "проєбав функцію")

    shift = None
    if shifr in shifr_with_num:
        shift_label = tk.Label(new_window, text="Введіть ключ:")
        shift_label.pack(pady=10)
        shift_entry = tk.Entry(new_window)
        shift_entry.pack(pady=10)
        shift = shift_entry

    # Кнопка для шифрування
    btn1 = tk.Button(
        new_window, text="Шифрувати", command=lambda: execute_command(first_command)
    )
    btn1.pack(pady=10)

    # Кнопка для дешифрування
    btn2 = tk.Button(
        new_window, text="Дешифрувати", command=lambda: execute_command(second_command)
    )
    btn2.pack(pady=10)

    # Кнопка для відкриття файлу
    open_file_btn = tk.Button(
        new_window, text="Відкрити файл", command=lambda: open_file(text_field)
    )
    open_file_btn.pack(pady=10)

    btn3 = tk.Button(new_window, text="Вийти", command=new_window.destroy)
    btn3.pack(pady=10)
