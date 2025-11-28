#include <stdio.h>

int main() {
    int arr[] = {1, 2, 4, 5, 6};
    int n = 6;  // numbers should be from 1 to 6
    int size = sizeof(arr) / sizeof(arr[0]);

    int expected_sum = n * (n + 1) / 2;
    int actual_sum = 0;

    for (int i = 0; i < size; i++)
        actual_sum += arr[i];

    int missing = expected_sum - actual_sum;

    printf("Missing Number: %d\n", missing);

    return 0;
}
