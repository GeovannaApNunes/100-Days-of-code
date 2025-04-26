number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
    
age = int(input("\nEnter your age:"))
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"The largest number is {num1}.")
    else:
        print(f"The largest number is {num3}.")    
else:
    if num2 >= num3:
        print("The largest number is {num2}.")
    else:
        print("The largest number is {num3}.")
                

number = int(input("\nEnter a positive number to calculate the sun up to that number: "))
sun = 0
for n in range(1, number + 1):
    sun =+ n
print(f"The sun of all numbers from 1 to {number} is {sun}")

number = int(input("\nEnter a number to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial of{number} is {factorial}.")

print("\nCongratulatios on complecting Day 5 of the 100 Days of Python Code Challenge!\n ")

