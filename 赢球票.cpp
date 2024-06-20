#include<stdio.h>
#include<stdlib.h>
#define Max 200 
typedef struct
{
	int data[Max];
	int length;
}sqList;

void InitList(sqList &L,int n,int data[])
{
	for(int i=1;i<=n;i++)
	{
		L.data[i]=data[i];
	}
	L.length=n;
}
void ListDelete(sqList &L,int t)
{	
	for(int j=t+1;j<=L.length;j++)
	{
		L.data[j-1]=L.data[j];
	}
	L.length--;
}
int search(sqList &L,int N,int data[])
{
	int sum1=0,sum2=0;
 	for(int i=1;i<=N;i++)
 	{
 		
 		int m=1;//mΪ�������� 
 		int j=i;//jΪ��ʼ��λ�� 
 		sum1=0;
 		InitList(L,N,data);
		 while(m<=N && L.length>0)
		{
			if(j>=L.length+1)j=1;
			printf("%2d",L.data[j]);
			if(L.data[j]==m)
			{
				m=1;
				sum1+=L.data[j];
				ListDelete(L,j);
		    }
		    else
		    {
		    	m+=1;
		   		j+=1;
			}
		   	
		    sum2=sum1>sum2?sum1:sum2;
		}
	 	putchar('\n');
	}
 	return sum2;
}

int main(){
	sqList L;
	int N;
	//���� 
	printf("��Ƭ��N:");
	scanf("%d",&N);
	int data[Max];
	for(int i=1;i<=N;i++)scanf("%d",&data[i]);
	printf("���ֵ:%d",search(L,N,data));
	return 0; 
}

