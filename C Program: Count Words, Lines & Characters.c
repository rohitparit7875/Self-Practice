#include <stdio.h>

int main() {
    char ch;
    int characters = 0, words = 0, lines = 0;
    int insideWord = 0;

    printf("Enter text (Press Ctrl + D to end):\n");

    while ((ch = getchar()) != EOF) {
        characters++;

        if (ch == '\n')
            lines++;

        if (ch == ' ' || ch == '\n' || ch == '\t') {
            insideWord = 0;
        } else if (insideWord == 0) {
            insideWord = 1;
            words++;
        }
    }

    printf("\nCharacters: %d\nWords: %d\nLines: %d\n", characters, words, lines);

    return 0;
}
