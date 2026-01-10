import datetime

now = datetime.datetime.now()
now_Y = now.year
now_M = now.month
now_D = now.day
year = int(input("you year  my bro:"))
mont = int(input("and mont"))
day = int(input("and day"))
if now_D < day:
    now_D = now_D + 30
    now_M = now_M - 1
if now_M < mont:
    now_M = now_M + 12
    now_Y = now_Y - 1
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
