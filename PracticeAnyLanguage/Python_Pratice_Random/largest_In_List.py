def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def largest_in_list(l):
    max = l[0]
    for i in range(5):
        if l[i] > max:
            max = l[i]
    return max
def main():
    l = []
    input_list(l)
    print("The Largest number in list is:", largest_in_list(l))

if __name__ == "__main__":
    main()