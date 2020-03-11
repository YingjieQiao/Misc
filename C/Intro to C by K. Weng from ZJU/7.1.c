#include <stdio.h>

int main(int argc, char *argv[]) {
	int n,swap,i,d;
	scanf("%d", &n);
	int arr[100];
	for (i = 0; i < n; i++){
		scanf("%d", &arr[i]);
	}
	for (i = 0 ; i < n-1 ; i++)
	{
		for (d = 0 ; d < n - i - 1; d++)
		{
			if (arr[d] > arr[d+1])
			{
				swap = arr[d];
				arr[d] = arr[d+1];
				arr[d+1] = swap;
			}
		}
	}
	for (i = 0; i < n; i++){
			printf("%d\t",arr[i]);
	}
	return 0;
}



