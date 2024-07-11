#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int B[10];
    int result = 0;
    int num;

    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &num);
        B[i] = num % 42;
    }

    for (int k = 0; k < 10; k++) {
        int count = 0;
        for (int j = k+1; j < 10; j++)
            if (B[k] == B[j])
                count++;
        if (count == 0)
            result++;
    }

    printf("%d\n", result);
    return 0;
}