#include <stdio.h>

int main()
{
  int t, c;
  printf("please enter the Beijing time: \n");
  scanf("%d",&t);
  c = t;
  if (c/1000)
  {
    t -= 800;
    printf("The UTC time is %d\n, today",t);
  }
  else if (c/100)
  {
    if (c >= 800)
    {
      t -= 800;
      printf("The UTC time is %d\n, today",t);
    }
    else
    {
      t = 2400-(800-t);
      printf("The UTC time is %d\n, yesterday",t);
    }
  }
  else if ((1<=c)&&(c<=99))
  {
    t = 2400-(800-t);
    printf("The UTC time is %d\n, yesterday",t);
  }
  else
  {
    printf("Your input is invalid.");
  }
}
