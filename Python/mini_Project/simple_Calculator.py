import math

while True:
    sign = input("Enter operation (+, -, *, /, %, **, sqrt) or type 'exit' to quit: ").strip().lower()
    
    if sign in ["exit", "quit", "q", "e"]:
        print("Goodbye!")
        break

    if sign == "sqrt":
        try:
            num = float(input("Enter a number for square root: "))
            if num < 0:
                print("Square root of negative numbers is not supported.")
            else:
                print(f"Square root of {num} is {math.sqrt(num):.2f}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if sign == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif sign == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif sign == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif sign == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                print(f"{num1} / {num2} = {num1 / num2:.2f}")
        elif sign == "%":
            if num2 == 0:
                print("Error: Modulus by zero is not allowed!")
            else:
                print(f"{num1} % {num2} = {num1 % num2}")
        elif sign == "**":
            print(f"{num1} ** {num2} = {num1 ** num2}")
        else:
            print("Invalid operator! Please choose a valid operation.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
