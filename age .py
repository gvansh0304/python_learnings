″
import datetime

birthYear=int(input("write you birth date and i will find your age"))
today = datetime.date.today()

year = today.year

print(year)

age = year-birthYear

print("Your age is:", age)
