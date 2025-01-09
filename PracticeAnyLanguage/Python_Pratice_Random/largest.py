def main():
    arr = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        arr.append(int(input(f"Enter the {i + 1} elements: ")))
    largest(arr)

def largest(arr):
    if not arr:
        print("Array is empty.")
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    print("Largest element is:",largest)

main()