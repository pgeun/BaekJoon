#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int A;
    scanf("%d", &A);

    int* B = (int*)malloc(sizeof(int) * A);
    for (int k = 0; k < A; k++)
    {
        scanf("%d", &B[k]);
    }

    int min = B[0];
    for (int i = 0; i < A; i++) {
        if (B[i] < min)
            min = B[i];
    }

    int max = B[0];
    for (int j = 0; j < A; j++) {
        if (B[j] > max)
            max = B[j];
    }

    free(B);

    printf("%d %d", min, max);

    return 0;
}