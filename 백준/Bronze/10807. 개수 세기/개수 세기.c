#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int A;
    scanf("%d", &A);

    int* C = (int*)malloc(sizeof(int) * A);

    for (int i = 0; i < A; i++) {
        scanf("%d", &C[i]);
    }

    int D;
    scanf("%d", &D);

    int E = 0;
    for (int j = 0; j < A; j++) {
        if (D == C[j]) {
            E += 1;
        }
    }

    printf("%d\n", E);

    free(C);
    return 0;
}