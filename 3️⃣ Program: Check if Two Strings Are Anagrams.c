#include <stdio.h>

int main() {
    char a[100], b[100];
    int count[256] = {0};
    int i;

    printf("Enter first string: ");
    fgets(a, sizeof(a), stdin);

    printf("Enter second string: ");
    fgets(b, sizeof(b), stdin);

    for (i = 0; a[i] != '\0'; i++)
        count[(unsigned char)a[i]]++;

    for (i = 0; b[i] != '\0'; i++)
        count[(unsigned char)b[i]]--;

    for (i = 0; i < 256; i++) {
        if (count[i] != 0) {
            printf("Not Anagrams\n");
            return 0;
        }
    }

    printf("Strings are Anagrams\n");
    return 0;
}
