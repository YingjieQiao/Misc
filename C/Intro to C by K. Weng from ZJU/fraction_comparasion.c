#include <stdio.h>

int main(int argc, char *argv[]) {
	int a1,a2,b1,b2,a3,b3;
	printf("Please enter the first fracttion in the format of x/y:\n");
	scanf("%d/%d",&a1,&a2);
	printf("Please enter the first fracttion in the format of x/y:\n");
	scanf("%d/%d",&b1,&b2);

	a3 = a2/a1;
	b3 = b2/b1;
	if (a3 > b3){
		printf("%d/%d < %d/%d",a1,a2,b1,b2);
	}
	else if(a3 < b3){
		printf("%d/%d > %d/%d",a1,a2,b1,b2);
	}
	else{
		printf("%d/%d = %d/%d",a1,a2,b1,b2);
	}
	return 0;
}