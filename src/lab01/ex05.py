fio = input("ФИО: ")
parts = fio.split()
initials = ""
for p in parts:
    initials = initials + p[0].upper()
initials = initials + "."
cl_fio = ""
for i in range(len(parts)):
    if i > 0:
        cl_fio = cl_fio + " "
    cl_fio = cl_fio + parts[i]
print("Инициалы:", initials)
print("Длина символов:", len(cl_fio))