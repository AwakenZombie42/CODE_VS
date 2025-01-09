def main():
    arr = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        arr.append(int(input(f"Enter the {i + 1} elements: ")))

    r = int(input("Enter the rotation: "))
    rotation(arr, r, size)

def rotation(arr, rotation, size):
    for i in range(rotation):
        temp = arr[0]
        for j in range(0, size - 1):
            arr[j] = arr[j + 1]
        arr[size - 1] = temp

    for i in range(size):
        print(arr[i]," ", end=" ")

main()