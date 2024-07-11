#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int B[30] = { 0 };

    int num;
    for (int i = 0; i < 28; i++)
    {
        scanf("%d", &num);
        B[num - 1] = num;
    }

    for (int k = 0; k < 30; k++)
        if (B[k] == 0) {
            B[k] = k + 1;
            printf("%d\n", B[k]);
        }

    return 0;
}
