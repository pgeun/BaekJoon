#include <stdio.h>
#include <string.h>

void Reverse(int* num, int* rvnum)
{
    int j = 2;
    for (int i = 0; i < 3; i++) {
        if (j >= 0 && j < 3) {
            rvnum[i] = num[j];
            j--;
        }
    }
}

void GetNum(int* num)
{
    for (int i = 0; i < 3; i++) {
        scanf("%1d", &num[i]);
    }
}

void MakeInt(int* rvnum, int* rvnum_f)
{
    *rvnum_f = 100 * rvnum[0] + 10 * rvnum[1] + rvnum[2];
}

int main()
{
    int num1[3], num2[3];
    GetNum(num1);
    GetNum(num2);

    int rvnum1[3] = { 0, };
    int rvnum2[3] = { 0, };
    Reverse(num1, rvnum1);
    Reverse(num2, rvnum2);

    int rvnum_f1;
    int rvnum_f2;
    MakeInt(rvnum1, &rvnum_f1);
    MakeInt(rvnum2, &rvnum_f2);

    if (rvnum_f1 > rvnum_f2)
        printf("%d", rvnum_f1);
    else
        printf("%d", rvnum_f2);

    return 0;
}