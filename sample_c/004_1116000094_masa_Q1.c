// compile : OK, execution : OK, output != txt
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    double a = atof(argv[1]), b = atof(argv[2]);

    printf("a/b = %lf\n", a / b);
    return 0;
}
