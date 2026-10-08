#include<stdio.h>
#include<listfun.h>
double ListVecdot(sadish *a, sadish *b){
          double val = 0;
          sadish *tempa=a, *tempb=b;
          while(tempa !=NULL){
                  val += tempa->data*tempb->data;
                  tempa = tempa->next;
                  tempb = tempb->next;
          }
         return val;
  }
int main(){
	ListVecdot(10,20);
	return 0;
}
