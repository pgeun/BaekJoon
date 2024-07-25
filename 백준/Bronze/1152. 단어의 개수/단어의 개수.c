#include <stdio.h>
#include <string.h>

int main()
{
    char sentence[1000000];
    scanf("%[^\n]s", sentence);
    int count = 0;
    if (strlen(sentence) == 1 && sentence[0] == ' ')
        printf("0");
    else {
        for (int i = 1; i < strlen(sentence) - 1; i++)
            if (sentence[i] == ' ')
                count++;
        printf("%d", count + 1);
    }
    
    return 0;
}