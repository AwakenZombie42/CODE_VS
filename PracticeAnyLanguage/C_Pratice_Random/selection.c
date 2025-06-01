#include <stdio.h>
#include <conio.h>
#define MAX_SIZE 100
int arr[MAX_SIZE];
int n, i, j, min, temp, count;
void selectionSort() {
    count = 0; // Initialize count to 0 before sorting
    for (i = 0; i <= n - 2; i++) {
        min = i;
        for (j = i + 1; j <= n - 1; j++) {
            count++;
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        // Swap the found minimum element with the first element
        temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}

void displayArray() {
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]); // Added space for better readability
    }
    printf("\n"); // Added newline for better output formatting
}

int main() {
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    // Fixed the condition to check for valid input
    if (n > MAX_SIZE || n <= 0) {
        printf("Invalid array size. Please enter a size between 1 and %d.\n", MAX_SIZE);
        return 1;
    }

    printf("Enter the elements of the array:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Array Before Sorting:\n");
    displayArray();

    selectionSort();

    printf("Array After Sorting:\n");
    displayArray();

    printf("Number of comparisons: %d\n", count); // Added a message for clarity
    getch();
    return 0;
}