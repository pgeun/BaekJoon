#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int B[9] = { 0 };
    for (int k = 0; k <= 8; k++)
    {
        scanf("%d", &B[k]);
    }

    int max = B[0];
    int index = 1;

    for (int i = 1; i <= 8; i++) {
        if (B[i] > max) {
            max = B[i];
            index = i + 1;
        }
    }

    printf("%d\n%d", max, index);

    return 0;
}
