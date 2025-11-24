#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int main() {
    int choice, x, y, result;
    int (*func_ptr)(int, int); // function pointer

    printf("Enter choice (1-Add, 2-Multiply): ");
    scanf("%d", &choice);

    printf("Enter two numbers: ");
    scanf("%d %d", &x, &y);

    if (choice == 1) {
        func_ptr = add;
    } else if (choice == 2) {
        func_ptr = multiply;
    } else {
        printf("Invalid choice!\n");
        return 0;
    }

    result = func_ptr(x, y);
    printf("Result = %d\n", result);

    return 0;
}
