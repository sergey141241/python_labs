def format_record(rec):
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    if type(fio) != str:
        raise TypeError("ФИО должно быть строкой")
    if type(group) != str:
        raise TypeError("группа должна быть строкой")
    if type(gpa) != float and type(gpa) != int:
        raise TypeError("GPA должно быть числом")

    parts = fio.split()

    if len(parts) < 2:
        raise ValueError("нужно хотя бы фамилия и имя")
    if group.strip() == "":
        raise ValueError("группа пустая")

    surname = parts[0].capitalize()

    initials = ""
    for i in range(1, len(parts)):
        letter = parts[i][0].upper()
        initials = initials + letter + "."

    group = group.strip()

    gpa_str = "{:.2f}".format(gpa)

    result = surname + " " + initials + ", гр. " + group + ", GPA " + gpa_str
    return result
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# Иванов И.И., гр. BIVT-25, GPA 4.60

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# Петров П., гр. IKBO-12, GPA 5.00

print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# Петров П.П., гр. IKBO-12, GPA 5.00

print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# Сидорова А.С., гр. ABB-01, GPA 4.00