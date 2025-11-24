#include <stdio.h>

int main() {
    char str[200];
    int i = 0, word_count = 0;
    int in_word = 0;  // 0 = false, 1 = true

    printf("Enter a sentence: ");
    fgets(str, sizeof(str), stdin);  // read line with spaces

    while (str[i] != '\0') {
        if (str[i] != ' ' && str[i] != '\n' && str[i] != '\t') {
            if (in_word == 0) {   // starting a new word
                in_word = 1;
                word_count++;
            }
        } else {
            in_word = 0;  // ended a word
        }
        i++;
    }

    printf("Number of words = %d\n", word_count);
    return 0;
}
