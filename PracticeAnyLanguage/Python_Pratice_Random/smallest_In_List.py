def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def smallest_in_list(l):
    min = l[0]
    for i in range(5):
        if l[i] < min:
            min = l[i]
    return min
def main():
    l = []
    input_list(l)
    print("The smallest number in list is:", smallest_in_list(l))

if __name__ == "__main__":
    main()