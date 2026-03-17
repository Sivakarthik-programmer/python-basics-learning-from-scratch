userInput = input ("Enter your number: ")

try:
    number = int(userInput)
    
    def oddEven (number):
        result = number % 2
        if result == 0:
            print("number is even") 
        else:
            print("number is odd")
    oddEven(number)
except ValueError:
    print("Enter valid number!!")