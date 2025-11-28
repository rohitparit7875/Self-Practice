#include <stdio.h>

int main() {
    int arr[] = {3, 5, 2, 3, 7, 5, 8};
    int size = sizeof(arr)/sizeof(arr[0]);
    
    printf("Duplicate elements: ");
    
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[i] == arr[j]) {
                printf("%d ", arr[i]);
                break;
            }
        }
    }
    return 0;
}
