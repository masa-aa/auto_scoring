// TimeOut
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int k = 1;
    while (k) {
        k++;
        if (k < 0)
            k = 1;
    }
    printf("%d", k);

    return 0;
}
