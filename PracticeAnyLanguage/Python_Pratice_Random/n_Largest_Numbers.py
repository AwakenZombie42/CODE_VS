def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def n_largest_numbers_in_list(l):
    l.sort()
    return l[-3:]

def main():
    l = []
    n = int(input("Enter number of largest numbers you want:"))
    size  = 0
    while size < n:
        size = int(input("Enter size of list: "))
    input_list(l)
    print("The Largest", n, "numbers in list is:", n_largest_numbers_in_list(l))

if __name__ == "__main__":
    main()