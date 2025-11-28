#include <stdio.h>

int main() {
    char str[200];
    int words = 0;

    printf("Enter a sentence: ");
    fgets(str, sizeof(str), stdin);

    for (int i = 0; str[i] != '\0'; i++) {
        if ((str[i] != ' ' && str[i] != '\n') &&
            (str[i+1] == ' ' || str[i+1] == '\0'))
            words++;
    }

    printf("Total words: %d\n", words);
    return 0;
}
