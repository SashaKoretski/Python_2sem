from math import floor
from tkinter import *
from tkinter import messagebox as mb
from per import *

E = 0.001
root = Tk()


def check_keys(text, action):  # Проверка на ввод
    return action != "1" or not any(char.isalpha() for char in text)


def exit_window():  # Функция выхода из приложения
    answer = mb.askokcancel(
        title="Внимание!",
        message="Вы действительно хотите выйти?"
    )
    if answer:
        root.destroy()


def developer_window():  # Информация о разработчике
    mb.showinfo("Информация об авторе", "Корецкий ИУ7-25Б")


def program_info_window():  # Информация о программе
    mb.showinfo("Информация о программе", "Калькулятор систем счисления.\n"
                                          "Переводит вещественное число из 10-й в 6-ю и обратно.")


def delete_all_entry():  # Удаление всех данных в строке
    entry_line.delete(0, "end")


def delete_all_out():  # Удаление всех данных в строке
    out_line.delete(0, "end")


def delete_all():  # Удаление всех данных
    delete_all_entry()
    delete_all_out()


def delete_last_entry():  # Удаление последнего элемента в строке
    entry_line.delete(len(entry_line.get()) - 1)
    delete_all_out()


def point_checker():  # Проверка, была ли введена точка
    value = entry_line.get()
    if "." in value:
        return 1
    return 0


def point_planter():  # Постановка точки
    if point_checker() == 0:
        entry_line.insert("end", ".")


def check_10_entry():  # Проверка введенного значения в 10-й СС
    value = entry_line.get()
    try:
        _ = float(value)
    except ValueError:
        mb.showerror("Ошибка", "Некорректный ввод!\n Должно быть введено вещественное число!")
        return 0
    else:
        return 1


def check_6_entry():  # Проверка введенного значения в 6-й СС
    value = entry_line.get()
    try:
        _ = float(value)
    except ValueError:
        mb.showerror("Ошибка", "Некорректный ввод!\n Должно быть введено вещественное число!")
        return 0
    for i in range(len(value)):
        if value[i] != "0" and value[i] != "1" and value[i] != "2" and value[i] != "3" \
                and value[i] != "4" and value[i] != "5" and value[i] != ".":
            mb.showerror("Ошибка", "Некорректный ввод!"
                                   "\n Должно быть введено вещественное число\n в 6-й системе счисления!")
            return 0
    value = value.split(".")
    if len(value) > 2:
        mb.showerror("Ошибка", "Некорректный ввод!"
                               "\n Должно быть введено вещественное число\n в 6-й системе счисления!")
        return 0
    return 1

def zero_delete():
    if entry_line.get() == "0":
        delete_all_entry()


def print_10_6():
    a, b = from_10_to_6(entry_line.get())
    delete_all_out()
    if b == "":
        out_line.insert("end", a)
    else:
        out_line.insert("end", str(a) + "." + b)


def print_6_10():
    a, b = from_6_to_10(entry_line.get())
    delete_all_out()
    if b == "":
        out_line.insert("end", a)
    else:
        out_line.insert("end", str(a) + "." + str(b))


entry_label = Label(text="Ввод: ").grid(row=0, column=0)
entry_line = Entry(root)
entry_line.grid(row=0, column=1, columnspan=5)
entry_line.config(validate="key", validatecommand=(entry_line.register(check_keys), "%P", "%d"))

out_label = Label(text="Вывод: ").grid(row=1, column=0)
out_line = Entry(root)
out_line.grid(row=1, column=1, columnspan=5)
out_line.config(validate="key", validatecommand=(out_line.register(check_keys), "%P", "%d"))
