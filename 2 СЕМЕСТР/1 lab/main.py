"""Корецкий ИУ7-25Б
Приложение - калькулятор систем счисления
Перевод заданного вещественного числа из 10-й системы счисления
в 6-ю и обратно"""

from math import floor
from tkinter import *
from tkinter import messagebox as mb
from func import *
from per import *

E = 0.1

root.config(bg="#FFF5AE")
root.title("Калькулятор систем счисления")  # Задаем название
root.geometry("320x145+700+400")  # Задаем размер окна
root.resizable(False, False)


# МЕНЮ


main_menu = Menu(root)
root.config(menu=main_menu)  # Создаем меню

operators_menu = Menu(
    main_menu,
    tearoff=0
)

change_notation_menu = Menu(
    operators_menu,
    tearoff=0
)

change_notation_menu.add_command(label="10 -> 6", command=print_10_6)
change_notation_menu.add_command(label="6 -> 10", command=print_6_10)

operators_menu.add_cascade(
    label="Перевод между системами счислений",
    menu=change_notation_menu
)

operators_menu.add_command(label="Очистить поле ввода", command=delete_all_entry)
operators_menu.add_command(label="Очистить поле вывода", command=delete_all_out)
operators_menu.add_command(label="Удалить последний элемент", command=delete_last_entry)
operators_menu.add_command(label="Очистить все", command=delete_all)

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
    label="Действия",
    menu=operators_menu
)
main_menu.add_cascade(
    label="Справка",
    menu=help_menu
)
main_menu.add_cascade(
    label="Выход",
    command=exit_window
)  # Задаем пункты меню

# КАЛЬКУЛЯТОР

Button(root, text="7", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "7"), delete_all_out()]) \
    .grid(row=2, column=0)

Button(root, text="8", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "8"), delete_all_out()]). \
    grid(row=2, column=1)

Button(root, text="9", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "9"), delete_all_out()]). \
    grid(row=2, column=2)

Button(root, text="4", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "4"), delete_all_out()]). \
    grid(row=3, column=0)

Button(root, text="5", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "5"), delete_all_out()]). \
    grid(row=3, column=1)

Button(root, text="6", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "6"), delete_all_out()]). \
    grid(row=3, column=2)

Button(root, text="1", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "1"), delete_all_out()]). \
    grid(row=4, column=0)

Button(root, text="2", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "2"), delete_all_out()]). \
    grid(row=4, column=1)

Button(root, text="3", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "3"), delete_all_out()]). \
    grid(row=4, column=2)

Button(root, text="0", width=10,
       bg="#FFD500", activebackground="#FFF5AE",
       command=lambda: [zero_delete(), entry_line.insert("end", "0"), delete_all_out()]). \
    grid(row=5, column=1)

Button(root, text=".", width=10,
       command=point_planter).grid(row=4, column=3)

Button(root, text="C1", command=delete_all_entry, width=10).grid(row=2, column=3)
# Button(root, text="c", command=delete_last_entry, width=10).grid(row=3, column=3)
Button(root, text="C2", command=delete_all_out, width=10).grid(row=3, column=3)
Button(root, text="C all", command=delete_all, width=10).grid(row=5, column=0)
Button(root, text="10->6", command=print_10_6, width=10).grid(row=5, column=2)
Button(root, text="6->10", command=print_6_10, width=10).grid(row=5, column=3)

root.mainloop()  # Отображаем окно
