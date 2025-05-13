def prime(s, e):
    for i in range(s, e + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)

def main():
    start = int(input("Enter a starting number: "))
    end = int(input("Enter an ending number: "))
    prime(start, end)

if __name__ == "__main__":
    main()