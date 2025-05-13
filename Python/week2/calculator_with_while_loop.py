# yes again but with a loop

while(True):
    sign = input("Enter operation:");
    if sign == "exit" or sign == "quit" or sign == "q" or sign == "Q" or sign == "e" or sign == "E" or sign == "EXIT" or sign == "QUIT":
        print("Goodbye");
        break;
    
    num1 = int(input("Enter a number:"));
    num2 = int(input("Enter another number:"));

    if sign == "+":
        print(num1 + num2);
    elif sign == "-":
        print(num1 - num2);
    elif sign == "*":
        print(num1 * num2);
    elif sign == "/":
        print(num1 / num2);
    elif sign == "%":
        print(num1 % num2);
    elif sign == "**":
        print(num1 ** num2);
    else:
        print("Invalid operator");