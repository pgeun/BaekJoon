#include <stdio.h>

int main() {
	int A, B;
	scanf("%d %d", &A, &B);
	int C;
	scanf("%d", &C);

	int D, E, F, G;
	D = B + C;
	if (D >= 60) {
		E = D / 60;
		A += E;
		if (A >= 24) {
			A -= 24;
			F = D % 60;
			B = F;
			printf("%d %d", A, F);
		}
		else {
			F = D % 60;
			B = F;
			printf("%d %d", A, F);
		}
	}
	else {
		printf("%d %d", A, B + C);
	}

	return 0;
}
