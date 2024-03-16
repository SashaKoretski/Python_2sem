from math import floor
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from per import *

root = Tk()

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
    mb.showinfo("Информация о программе", "Стеганография.")

def select_file():
    filetypes = (
        ('JPG files', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Выбранный файл',
        message=filename
    )
    return filename

def file_message():
    if file_info_entry.get() == "":
        mb.showerror(
            title='Внимание!',
            message="Файл не выбран"
        )

entry_label = Label(text="Ввод текста для шифрования: ").grid(row=0, column=1)
entry_line = Text(height=6, width=64)
entry_line.grid(columnspan=3)

file_info_label = Label(text="Файл для шифрования: ").grid(row=8, column=0)
file_info_entry = Entry(state="readonly", width=30)
file_info_entry.grid(row=8, column=1)

out_label = Label(text="Вывод расшифрованного текста: ").grid(row=10, column=1)
out_line = Text(height=6, width=64)
out_line.grid(columnspan=3)