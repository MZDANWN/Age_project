import datetime
import calendar

R = "\033[31m"
Y = "\033[33m"
G = "\033[32m"
now = datetime.datetime.now()
now_Y = now.year
now_M = now.month
now_D = now.day

year = int(input(f"{Y}you year: {R}"))
if now_Y < year:
    print("Enter a valid year")
    exit()
mont = int(input(f"{Y}and mont: {R}"))
if mont < 1 or mont > 12:
    print("month from 1 to 12")
    exit()
day = int(input(f"{Y}and day: {R}"))
max_day = calendar.monthrange(year, mont)[1]
if day < 1 or day > max_day:
    print(f"This month there is only {max_day} days")
    exit()

if day == 29 and mont == 2:
    if not calendar.isleap(year):
        print("This day is not available")
        exit()
if now_D < day:
    now_D = now_D + calendar.monthrange(now_Y, now_M)[1]
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
print(f"{G}Your age is: {Y}{year} {G}years / {Y}{mont} {G}months / {Y}{day} {G}days")
