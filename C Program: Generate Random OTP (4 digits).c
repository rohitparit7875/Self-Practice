#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int otp;

    srand(time(NULL));
    otp = rand() % 9000 + 1000;  // ensures 4 digits

    printf("Your OTP is: %d\n", otp);

    return 0;
}
