firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

Choice = input("Enter your choice (1/2/3/4): ")

if Choice == '1':
    def add(firstNumber, secondNumber):
        result =  firstNumber + secondNumber
        return result
    print("Result: ", add(firstNumber, secondNumber))
elif Choice == '2':
    def subtract(firstNumber, secondNumber):
        result = firstNumber - secondNumber
        return result
    print("Result: ", subtract(firstNumber, secondNumber))  
elif Choice == '3':
    def multiply(firstNumber, secondNumber):
        result = firstNumber * secondNumber
        return result
    print("Result: ", multiply(firstNumber, secondNumber))

elif Choice == '4':
    try:
        def divide(firstNumber, secondNumber):
            if secondNumber != 0:
                result = firstNumber / secondNumber
                return result
            else:
                return "Cannot divide by zero"
    except ZeroDivisionError:
        print("Cannot divide by zero")
    print("Result: ", divide(firstNumber, secondNumber))
