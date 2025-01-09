def main():
    harshad()

def harshad():
    num = input("Enter a number: ")
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    if int(num) % sum == 0:
        print(num, "is a Harshad number.")
    else:
        print(num, "is not a Harshad number.")

if __name__ == "__main__":
    main()