def main():
    num = input("Enter a number: ")
    happy(num)

def happy(num):
    seem = [] # seem = set()
    sum = 0
    c = num
    while sum != 1 and num not in seem:
        seem.append(num) # seem.add(num)
        sum = 0
        for i in range(len(num)):
            sum += int(num[i])**2
        num = str(sum)

    if sum == 1:
        print(c, "is a happy number.")
    else:
        print(c, "is not a happy number.")

if __name__ == "__main__":
    main()

'''
num = 19 is a string
1 9 
0 1

1^2 + 9^2 = 82 = sum is a integer

num = 82 is a string
8 2
0 1

8^2 + 2^2 = 68 = sum is a integer

num = 68 is a string
6 8
0 1

6^2 + 8^2 = 100 = sum is a integer

num = 100 is a string
1 0 0
0 1 2

1^2 + 0^2 + 0^2 = 1 = sum is a integer

num = 1 is a string

11 -> 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4.... -> 16 loop

list = [11, 2, 4, 16, 37, 58, 89, 145, 42, 20]
'''