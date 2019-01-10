#include<stdio.h>
int main()
{
	int result=0;
	int i=0;
	char ch;
	do{
		scanf("%d",&i);
		result^=i;
	}while(ch=(getchar())!='\n');
	printf("%d",result);
	return 0;
}
