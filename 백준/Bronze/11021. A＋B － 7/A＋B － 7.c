#include <stdio.h>

int main() {
	int A;
	scanf("%d", &A);

	for (int i = 0; i < A; i++)
	{
		int B, C = 0;
		scanf("%d %d", &B, &C);
		printf("Case #%d: %d\n",i+1, B+C);
	}

	return 0;
}
