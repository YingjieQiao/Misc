#include <stdio.h>

int max(int a[], int len)
{
  int maxid = 0;
  for ( int i = 1; i<len; i++)
  {
    if(a[i]>a[maxid])
    {
      maxid = i;
    }
  }
  return maxid;
}

int main()
{
  int amount[] = {1,2,4,435,123,546,76,433,12,676,44,66,88,97};
  int len = sizeof(amount)/sizeof(amount[0]);

  for (int i=len-1; i>0; i++)
  {
    int maxid = max(amount, sizeof(amount)/sizeof(amount[0]));
    //swap a[maxid] a[len-1]
    int t =amount[maxid];
    amount[maxid] = amount[len-1];
    amount[len-1] = t;
  }

  for (int i=0; i<len; i++)
  {
    printf("%d\n", amount[i]);
  }
  return 0;
}
