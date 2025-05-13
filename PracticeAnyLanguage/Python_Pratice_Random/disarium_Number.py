def main():
    num = input("Enter a number: ")
    disarium(num)

def disarium(num):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i]) ** (i + 1)

    if sum == int(num):
        print(num, "is a Disarium number.")
    else:
        print(num, "is not a Disarium number.")

if __name__ == "__main__":
    main()