1#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    if (!fgets(str, sizeof(str), stdin)) return 1;
    // remove newline if present
    size_t len = strlen(str);
    if (len > 0 && str[len-1] == '\n') str[--len] = '\0';

    char *l = str;
    char *r = str + len - 1;
    while (l < r) {
        char tmp = *l;
        *l = *r;
        *r = tmp;
        l++; r--;
    }

    printf("Reversed: %s\n", str);
    return 0;
}
