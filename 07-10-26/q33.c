#include<stdio.h>
int n=30;
void swap(int a , int b){
	int temp=a;
	a=b;
	b=temp
void fun(int arr[n]){
	for(int i=0;i<=n-2;i++){
        for (int j=0;j<=n-i-2;j++){
		if(arr[j]>arr[j+1]){
			swap(arr[j],arr[j+1]);}}}
	}

int main(){





}
