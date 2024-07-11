#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int* B = (int*)calloc(N, sizeof(int));
    int N1, N2, m;
    for (int i = 0; i < M; i++)
    {
        scanf("%d %d %d", &N1, &N2, &m);
        for (int j = N1-1; j < N2; j++)
            B[j] = m;
    }

    for (int k = 0; k < N; k++)
        printf("%d ", B[k]);

    free(B);

    return 0;
}