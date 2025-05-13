import math
def input_cof():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    return a, b, c

def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Root :", root)
    else:
        real_part = -b / (2*a)
        ima_part = math.sqrt(-discriminant) / (2*a)
        print("Root 1:", real_part, "+", ima_part, "i")
        print("Root 2:", real_part, "-", ima_part, "i")

def main():
    a, b, c = input_cof()
    quadratic(a, b, c)

if __name__ == "__main__":
    main()