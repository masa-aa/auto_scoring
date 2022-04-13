// compile : OK, execution : NG
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int a = atoi(argv[1]), b = atoi(argv[2]);

    printf("a/(b-2) = %d\n", a / (b - 2));
    return 0;
}
