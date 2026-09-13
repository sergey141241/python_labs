fio = input("ФИО: ")
parts = fio.split()
initials = ""
for p in parts:
    initials = initials + p[0].upper()
initials = initials + "."
clean_fio = ""
for i in range(len(parts)):
    if i > 0:
        clean_fio = clean_fio + " "
    clean_fio = clean_fio + parts[i]
print("Инициалы:", initials)
print("Длина (символов):", len(clean_fio))