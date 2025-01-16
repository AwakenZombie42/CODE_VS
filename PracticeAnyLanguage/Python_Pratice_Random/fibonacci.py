def fibonacci(n):
    if n < 0:
        return "Please enter a positive integer."
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter a number: "))
    for i in range(0, n):
        print(fibonacci(i), end = " ")

if __name__ == "__main__":
    main()