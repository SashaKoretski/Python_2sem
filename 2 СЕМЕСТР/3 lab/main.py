from math import floor
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from func import *
from per import *

E = 0.1

root.config(bg="#FFF5AE")
root.title("Стеганография")  # Задаем название
root.geometry("515x300")  # Задаем размер окна
# root.resizable(False, False)

# МЕНЮ

main_menu = Menu(root)
root.config(menu=main_menu)  # Создаем меню

operators_menu = Menu(
    main_menu,
    tearoff=0
)

help_menu = Menu(
    main_menu,
    tearoff=0
)
help_menu.add_command(
    label="О разработчике",
    command=developer_window
)
help_menu.add_command(
    label="О программе",
    command=program_info_window
)  # Задаем подпункты меню

main_menu.add_cascade(
    label="Справка",
    menu=help_menu
)
main_menu.add_cascade(
    label="Выход",
    command=exit_window
)  # Задаем пункты меню

#####################################

Button(root, text='Выбор файла',
    command=lambda:[file_info_entry.config(state="normal"),
                    file_info_entry.insert("end", select_file()),
                    file_info_entry.config(state="readonly")]
).grid(row=9, column=0)

Button(root, text="Зашифровать текст", width=20,
       bg="#FFD500", activebackground="#FFF5AE", command=lambda:file_message()).grid(row=9, column=1)

Button(root, text="Расшифровать текст", width=20,
       bg="#FFD500", activebackground="#FFF5AE", command=lambda:file_message()).grid(row=9, column=2)

root.mainloop()  # Отображаем окно
