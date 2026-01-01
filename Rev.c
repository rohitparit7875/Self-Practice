#include <stdio.h>

int main() {
    char str[100];
    char *start, *end, temp;

    printf("Enter a string: ");
    gets(str);   // for exam use; avoid in real projects

    start = str;
    end = str;

    while (*end != '\0')
        end++;
    end--;  // last character

    while (start < end) {
        temp
