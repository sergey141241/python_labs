m = int(input("Минуты: "))

hours = m // 60
minutes = m % 60

if minutes < 10:
    print(hours, ":0", minutes, sep="")
else:
    print(hours, ":", minutes, sep="")