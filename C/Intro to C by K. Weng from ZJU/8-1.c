#include <stdio.h>
#include <string.h>

main(){
  int count=0,i;
  char s[1024];
  gets(s);

  for (i = 0; s[i] != '\0'; i++)
  {
    if (s[i] != ' ' && s[i] != '.')
    {
      count++;
    }
    else if (s[i] == ' ' || s[i] == '.')
    {
      if (count)
      {
      printf("%d\n", count);
      count = 0;
      }
    }
  }
  return 0;
}
