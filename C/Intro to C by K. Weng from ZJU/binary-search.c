#include <stdio.h>

//binary search
//times of search = log2(n)
//on condition that this array is already sorted

int search(int key, int a[], int len)
{
  int left = 0, right = len - 1,mid;
  int ret;
  while( left < right)
  {
    mid = (left+right)/2;
    if( a[mid] == key)
    {
      ret = mid;
      break;
    }
    else if( a[mid] > key)
    {
      right = mid - 1;
    }
    else
    {
      left = mid + 1;
    }
  }
  return ret;
}

int main()
{
  int k = 76;
  int amount[] = {1,2,4,435,123,546,76,433,12,676,44,66,88,97};
  int r = search(k, amount, sizeof(amount)/sizeof(amount[0]));

  printf("%d\n",r);
  return 0;
}
