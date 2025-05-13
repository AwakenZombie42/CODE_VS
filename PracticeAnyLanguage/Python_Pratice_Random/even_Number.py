def input_list(l):
    for i in range(5):
        l.append(int(input(f"Enter the element {i + 1}: ")))

def even_number(l):
    for i in range(5):
        if l[i] % 2 == 0:
            print(l[i])
def main():
    l = []
    input_list(l)
    even_number(l)

if __name__ == "__main__":
    main()