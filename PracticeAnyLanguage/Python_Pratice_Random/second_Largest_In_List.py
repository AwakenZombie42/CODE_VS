def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def second_largest_in_list(l):
    l.sort(reverse=True)
    if len(l) >= 2:
        return l[1]
    else:
        return -1
def main():
    l = []
    input_list(l)
    print("The Second Largest number in list is:", second_largest_in_list(l))

if __name__ == "__main__":
    main()