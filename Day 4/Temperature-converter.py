def celsiusToFahrenheit(temp):
    result = temp * 9/5 + 32
    return result
def fahrenheitToCelsius(farahent):
    result = (farahent - 32) * 5/9
    return result
try:
    choice = input("Enter your choice: ")

    if choice == '1':
        temp = float(input("Enter temperature in Celcius: "))
        print("Temperature in Farahent: ", celsiusToFahrenheit(temp))
    elif choice == '2':        
        temp = float(input("Enter temperature in Farahent: "))
        print("Temperature in Celcius: ", fahrenheitToCelsius(temp))
    else:
        print("Invalid choice! Enter 1 or 2 only!")
except ValueError:
    print("Invalid input. Please enter a valid number.")