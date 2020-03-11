#include <stdio.h>

int n; //n is a global variable.
int Findrowmax(int onerow[]){
  int i,max = onerow[0],max_index;
  for (i=0;i<n;i++)
  {
    if (onerow[i] > max)
    {
      max = onerow[i];
      max_index = i;
    }
  }
  return max_index;
}

int Findcolmin(int num[][n], int col){
  int min = num[0][col],i;
  for (i=0;i<n;i++)
  {
    if (num[i][col] < min)
    {
      min = num[i][col];
    }
  }
  return min;
}

main(){
  int i,j,x,col,flag=0;

  printf("Please enter the size of the matrix.\n");
  scanf("%d",&n);
  int num[n][n];

  for (i=0;i<n;i++)
  {
    for (j=0;j<n;j++)
    {
      printf("Please enter a number.\n");
      scanf("%d",&x);
      num[i][j] = x;
    }
  }

  for (i=0;i<n;i++)
  {
    col = Findrowmax(num[i]);
    if (num[i][col] == Findcolmin(num,col))
    {
      printf("%d %d\n", i, col);
      flag = 1;
      break;
    }
  }

  if (!flag)
  {
    printf("This matrix does not have a such point.\n");
    return 0;
  }
}
