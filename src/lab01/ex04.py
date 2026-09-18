m = int(input("Минуты: "))
days = m // 1440
ost = m % 1440
hours = ost // 60
minutes = ost % 60
if minutes < 10:
    print(days, " д ", hours, ":0", minutes, sep="")
else:
    print(days, " д ", hours, ":", minutes, sep="")