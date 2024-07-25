#include <stdio.h>
#include <string.h>

int main()
{
    int count = 0;
    scanf("%d", &count);

    for (int i = 0; i < count; i++) {
        int num = 0;
        char word[20];
        scanf("%d %s", &num, word);
        for (int j = 0; j < strlen(word); j++) {
            for (int k = 0; k < num; k++) {
                printf("%c", word[j]);
            }
        }
        printf("\n");
    }
    return 0;
}