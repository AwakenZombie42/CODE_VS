def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def product_of_list(l):
    prod = 1
    for i in range(5):
        prod = prod * l[i]
    return prod
def main():
    l = []
    input_list(l)
    print("The Product of the list is:", product_of_list(l))

if __name__ == "__main__":
    main()