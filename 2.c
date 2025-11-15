#include <stdio.h>
#include <stdlib.h>

int main() {
    int r1, c1, r2, c2;
    printf("Enter rows and cols of matrix A: ");
    if (scanf("%d %d", &r1, &c1) != 2) return 1;
    printf("Enter rows and cols of matrix B: ");
    if (scanf("%d %d", &r2, &c2) != 2) return 1;

    if (c1 != r2) {
        printf("Matrix multiplication not possible (c1 must equal r2).\n");
        return 1;
    }

    int i, j, k;
    int **A = malloc(r1 * sizeof(int*));
    int **B = malloc(r2 * sizeof(int*));
    int **C = malloc(r1 * sizeof(int*));
    for (i = 0; i < r1; ++i) A[i] = malloc(c1 * sizeof(int));
    for (i = 0; i < r2; ++i) B[i] = malloc(c2 * sizeof(int));
    for (i = 0; i < r1; ++i) C[i] = calloc(c2, sizeof(int));

    printf("Enter elements of A (%d x %d):\n", r1, c1);
    for (i = 0; i < r1; ++i)
        for (j = 0; j < c1; ++j)
            scanf("%d", &A[i][j]);

    printf("Enter elements of B (%d x %d):\n", r2, c2);
    for (i = 0; i < r2; ++i)
        for (j = 0; j < c2; ++j)
            scanf("%d", &B[i][j]);

    // multiply
    for (i = 0; i < r1; ++i) {
        for (j = 0; j < c2; ++j) {
            for (k = 0; k < c1; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    printf("Result matrix (%d x %d):\n", r1, c2);
    for (i = 0; i < r1; ++i) {
        for (j = 0; j < c2; ++j) printf("%d ", C[i][j]);
        printf("\n");
    }

    // free memory
    for (i = 0; i < r1; ++i) { free(A[i]); free(C[i]); }
    for (i = 0; i < r2; ++i) free(B[i]);
    free(A); free(B); free(C);

    return 0;
}
