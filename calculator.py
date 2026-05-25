import math

print("=================================")
print("      Advanced Calculator")
print("=================================")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")
print("7. square")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 + num2

    print("Result =", round(result, 2))

elif choice == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 - num2

    print("Result =", round(result, 2))

elif choice == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 * num2

    print("Result =", round(result, 2))

elif choice == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 != 0:
        result = num1 / num2
        print("Result =", round(result, 2))
    else:
        print("Error! Division by zero is not allowed.")

elif choice == 5:
    num1 = float(input("Enter base number: "))
    num2 = float(input("Enter power: "))

    result = math.pow(num1, num2)

    print("Result =", round(result, 2))

elif choice == 6:
    num1 = float(input("Enter a number: "))

    if num1 >= 0:
        result = math.sqrt(num1)
        print("Square Root =", round(result, 2))
        
 elif choice==7:
    num1=float(input("enter a number: "))
   
   
    result=num1**2
    print("Square =", round(result, 2))

    else:
        print("Error! Cannot find square root of negative number.")

else:
    print("Invalid Choice!")
