#include <stdio.h>

int main() {
	int A;
	scanf("%d", &A);

	for (int i = 0; i < A; i++)
	{
		int B = 0;
		while (B != i+1)
		{
			printf("*");
			B += 1;
		}
		printf("\n");
	}

	return 0;
}