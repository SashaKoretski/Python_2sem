from math import floor

E = 0.1

def from_6_to_10(str_en):  # Перевод из 6-й в 10-ую СС
    value = str_en.split(".")
    if value[0] == "":
        value[0] = "0"
    value[0] = int(value[0])
    fin_10 = 0
    i = 0
    while value[0] > 0:
        fin_10 += (value[0] % 10) * (6 ** i)
        value[0] //= 10
        i += 1
    # delete_all_out()
    # out_line.insert("end", fin_10)

    drb_10 = ""
    if len(value) == 2 and len(value[1]) != 0:
        # out_line.insert("end", ".")
        le = len(value[1])
        value[1] = int(value[1])

        drb_10 = 0
        for j in range(le, 0, -1):
            drb_10 += (value[1] % 10) * ((1 / 6) ** j)
            value[1] //= 10
        drb_10 *= 10 ** 6
        drb_10 = round(drb_10)
        # out_line.insert("end", drb_10)
    return fin_10, drb_10


def from_10_to_6(str_en):  # Перевод из 10-й в 6-ую СС
    value = str_en.split(".")
    if value[0] == "":
        value[0] = "0"

    # try:
    #     value[0] = int(value[0])
    # except ValueError:
    #     mb.showerror("Ошибка", "Переполнение!")
    value[0] = int(value[0])
    fin_6 = 0
    i = 0
    while value[0] > 0:
        fin_6 += (value[0] % 6) * (10 ** i)
        value[0] //= 6
        i += 1
    # delete_all_out()
    # out_line.insert("end", fin_6)
    drb_6 = ""  # Строка с дробной частью в 6-й СС
    if len(value) == 2 and len(value[1]) != 0:
        # out_line.insert("end", ".")
        le = len(value[1])

        k = 0
        while value[1][0] == "0":
            k += 1
            value[1] = value[1][1:]

        # try:
        #     value[1] = int(value[1])
        # except ValueError:
        #     mb.showerror("Ошибка", "Переполнение!")
        value[1] = int(value[1])
        value[1] /= 10 ** (le - k)

        while value[1] > E:
            value[1] *= 6
            drb_6 += str(floor(value[1]))
            value[1] = value[1] % 1
        # out_line.insert("end", drb_6[0:6])
    return fin_6, drb_6[0:6]
