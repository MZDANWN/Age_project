import datetime

R = "\033[31m"
Y = "\033[33m"
G = "\033[32m"
now = datetime.datetime.now()
now_Y = now.year
now_M = now.month
now_D = now.day
year = int(input(f"{Y}you year  my bro: " f"{R}"))
mont = int(input(f"{Y}and mont: " f"{R}"))
day = int(input(f"{Y}and day: " f"{R}"))
if now_D < day:
    now_D = now_D + 30
    now_M = now_M - 1
if now_M < mont:
    now_M = now_M + 12
    now_Y = now_Y - 1
if year > now_Y:
    year = year - now_Y
else:
    year = now_Y - year
if mont > now_M:
    mont = mont - now_M
else:
    mont = now_M - mont
if day > now_D:
    day = day - now_D
else:
    day = now_D - day
print("your age is " + str(year) + "yer/" + str(mont) + "month/" + str(day) + "day")
