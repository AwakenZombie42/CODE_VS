def table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

def main():
    num = int(input("Enter a number: "))
    table(num)

if __name__ == "__main__":
    main()