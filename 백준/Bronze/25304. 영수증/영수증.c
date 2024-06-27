#include <stdio.h>

int main() {
	int A;
	scanf("%d", &A);
	int B;
	scanf("%d", &B);

	int C, D, E = 0;
	while (B != 0) {
		scanf("%d %d", &C, &D);
		E += C * D;
		B -= 1;
	}
	if (A == E) {
		printf("Yes");
	}
	else {
		printf("No");
	}
	return 0;
}