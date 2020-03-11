#include <stdio.h>

main(){
  int a,b,i,ans;

  scanf("%d %d",&a, &b);
  do {
    ans = (a*10)/b;
    printf("%d",ans);
    a = (a*10)%b;
    i++;
  } while(a && i<=200);

  return 0;
}
