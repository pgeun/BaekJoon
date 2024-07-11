#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int* B = (int*)calloc(N, sizeof(int));
    for (int j = 0; j < N; j++)
        B[j] = j + 1;

    int N1, N2, tmp;
    for (int i = 0; i < M; i++)
    {
        scanf("%d %d", &N1, &N2);
        tmp = B[N1-1];
        B[N1-1] = B[N2-1];
        B[N2-1] = tmp;
    }

    for (int k = 0; k < N; k++)
        printf("%d ", B[k]);

    free(B);

    return 0;
}