#include <stdio.h>

main(){
  int n,digit;
  int i=0,j=0;
  char ans[100];

  scanf("%d", &n);
    while (n)
    {
        digit = n % 10;
        i++;
        if (digit % 2 == i % 2)
        {
            ans[j++]=1;
        }
        else
        {
            ans[j++]=0;
        }
        n /= 10;
    }
    int array_size = sizeof(ans);
    for (int m = 0; m < j; m++)
    printf("%d", ans[m]);
    return 0;
}
