#include <stdio.h>
#include <string.h>


int IsPrime(int n){
    int i;
    if (n == 2)
    {
        return 1;
    }
    if (n % 2 == 0)
    {
        return 0;
    }
    for (i = 3; i < n/2; i += 2)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

char prime(int n,char l[]){
    int i,j=1;
    char l[1024];
    l[0] = 1;
    while (!IsPrime(n))
    {
        for (i = 2; i < n; i++)
        {
            if (IsPrime(i) && n % i == 0)
            {
                l[j++] = i;
                break;
            }
        }
        n /= i;
    }
    l[j++] = n;
    return l[1024];
}



main(){
  int n,d;
  char nl[1024],dl[1024];
  scanf("%d/%d", &n, &d);
  strcpy(nl,prime(n,nl[1024]));
  strcpy(dl,prime(d,dl[1024]));
  printf("%s\n",nl);
  printf("%s\n",dl);
  return 0;
}
