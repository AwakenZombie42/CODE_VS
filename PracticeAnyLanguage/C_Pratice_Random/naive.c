#include <stdio.h>
#include <conio.h>
#include <string.h>
void naive_string_matcher(char T[], char P[]) {
	int n, m, i, j, found;
	n = strlen(T);
	m = strlen(P);
	found = 0;
	for (i = 0; i <= n - m; i++) {
		j = 0;
		while (j < m && T[i + j] == P[j]) {
			j++;
		}
		if (j == m) {
			printf("Pattern found at index %d\n", i);
			found = 1;
		}
	}
	if (!found) {
		printf("No valid shift exists, i.e., there is no substring of T matching P.\n");
	}
}
int main() {
	char T[1000], P[1000];
	printf("Enter the text (T): ");
	scanf("%s", T);
	printf("Enter the pattern (P): ");
	scanf("%s", P);
	naive_string_matcher(T, P);
	getch();
	return 0;
}