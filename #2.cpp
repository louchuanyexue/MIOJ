#include<stdio.h>
int main()
{
	int a[256]={0};
	int i=0;
	char ch;
	do{
		scanf("%d",&i);
		a[i]+=1;
	 }while((ch=getchar())!='\n');
	for(i=0;i<256;i++){
		if(a[i]==1){
			printf("%d",i);
		}
	}
	return 0;
}
