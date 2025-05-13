def main():
    disarium()

def disarium():
    count = 0
    for i in range(0, 101):
        string_number = str(i)
        sum = 0
        for j in range(len(string_number)):
            sum += int(string_number[j]) ** (j + 1)

        if sum == int(string_number):
            print(string_number, "is a Disarium number.")
            count += 1
        else:
            print(string_number, "is not a Disarium number.")

    print("Number of Disarium numbers between 0 and 100:", count)

if __name__ == "__main__":
    main()