#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
        if (argc < 3) {
                printf("not enough args\n");
                return -1;
        }

        int lhs = atoi(argv[1]);
        int rhs = atoi(argv[2]);

        printf("%i\n", lhs * rhs);
        return 0;
}
