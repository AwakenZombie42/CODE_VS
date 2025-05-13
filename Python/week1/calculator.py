# A calculator in python no shit what you thought

num1 = int(input("Enter a number:"));
sign = input("Enter operator:");
num2 = int(input("Enter another number:"));

if sign == "+":
    print(num1 + num2);
elif sign == "-":
    print(num1 - num2);
elif sign == "*":
    print(num1 * num2);
elif sign == "/":
    print(num1 / num2);
else:
    print("Invalid operator");