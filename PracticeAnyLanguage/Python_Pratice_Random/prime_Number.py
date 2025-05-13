def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))

    if prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

if __name__ == "__main__":
    main()