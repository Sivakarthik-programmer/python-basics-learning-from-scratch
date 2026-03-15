print("Hello World")

name = input("Enter your name: ")
print("Hello", name)
number = int(input("Enter a number: "))
# def factorial(number):
#     if number == 0:
#         return 1
#     return number * factorial(number - 1)
# print("Factorial for 5 is ", factorial(number))


if number > 0:
    print("The Entered numnber is Positive")
elif number < 0:
    print("Entered number is Negative")
else:
    print("Entered number is Zero")