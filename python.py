numbers = [1,2]
print("hello I can ansere your addishin qustin")
Sum = sum(numbers)

x = input("Type first number: ")
y = input("Type second number: ")

sum = int(x)+ int(y)

print("The sum is: ", sum)


print("Hello, How Can I help you?")
b = int(input("Is your number greator than 10 or not? Enter a number and I will answer it for you: "))
a=10
if a>b:
    print("You have enter {0} that is less than 10".format(b))
elif a<b:
    print("You have enter {0} that is more than 10".format(b))
else:
    print("You have enter {0} that is equal to 10".format(b))


decision = input("Do you want to continue, press n to exit?")
if decision =="n":
   quit()
else:
   print("Superb! Let continue") 

print("Superb! Let find now if a number is odd,even")
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

print("Superb! Lets continue more... Let find now if a number is positive, negative or zero?")
num = float(input("Enter a number: "))
# Input: 1.2
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")







