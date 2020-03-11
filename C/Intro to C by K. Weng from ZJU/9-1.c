#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10000

int main()
{
  char tar[MAX], sour[MAX];
  printf("Please enter the target string.\n");
  gets(tar);
  printf("Please enter the source string.\n");
  gets(sour);

  char *p = sour;
  int output = 0;
  while (*p != '/0')
  {
    p = strstr(p, tar);
    if (!p)
    {
      break;
    }
    printf("%s\n",p);
    printf("%d\n", p-sour);
    output = 1;
    p++;
  }
  if (!output)
    {
        printf("-1");
    }
  putchar('\n');
  return 0;
}
