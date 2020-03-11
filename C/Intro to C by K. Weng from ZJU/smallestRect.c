#include <stdio.h>

int cmp(const void *a, const void *b)
{
	return *(int *)a - *(int *)b;
}

int main(int argc, char const *argv[])
{
	int n;
	scanf("%d", &n);
	int x[n], y[n];
	for (int i = 0; i != n; ++i)
		scanf("%d %d", &x[i], &y[i]);
	qsort(x, n, sizeof(x[0]), cmp);
	qsort(y, n, sizeof(x[0]), cmp);
	printf("%d %d %d %d\n", x[0], y[0], x[n-1], y[n-1]);
	return 0;
}