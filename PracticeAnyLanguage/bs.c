#include <stdio.h>

#define N 5

int a[N];

void binary_search() {
    int n, first = 0, last = N - 1, mid, found = -1;
    
    printf("Enter the number that needs to be searched:");
    scanf("%d", &n);
    printf("\n");
    int count = 0;
    while (first <= last) {
        mid = (first + last) / 2;
        count++;
        if (a[mid] == n) {
            found = mid;  // Store the found index
            printf("comparision %d\n", count);
            break;
        } else if (a[mid] < n) {
            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }
    
    if (found != -1) {
        printf("Number found at index %d\n", found);
    } else {
        printf("Number not found\n");
    }
}

int main() {
    int i, j, choice;
    
    printf("Enter %d numbers:", N);
    for (i = 0; i < N; i++) {
        scanf("%d", &a[i]);
    }
    printf("\n");
    binary_search();

    return 0;
}
