#include<stdio.h>
void run(int n,char*s)
{
	printf("%s %d\n",s,n);
	for(;n--;s++)fputc(*s,stdout);
	fputc('\n',stdout);
}
