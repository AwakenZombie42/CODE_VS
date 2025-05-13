def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def sum_list(l):
    sum = 0
    for i in range(5):
        sum = sum + l[i]
    return sum

def main():
    l = []
    input_list(l)
    print("The sum of the list is:", sum_list(l))

if __name__ == "__main__":
    main()