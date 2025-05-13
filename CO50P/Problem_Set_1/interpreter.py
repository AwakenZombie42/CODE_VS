expression = input("Expression: ")

if "+" in expression:
    a, b = expression.split("+")
    print(int(a) + int(b))

elif "-" in expression:
    a, b = expression.split("-")
    print(int(a) - int(b))

elif "*" in expression:
    a, b = expression.split("*")
    print(int(a) * int(b))

elif "/" in expression:
    a, b = expression.split("/")
    print(int(a) / int(b))