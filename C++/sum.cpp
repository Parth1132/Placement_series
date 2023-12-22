#include<iostream>
using namespace std;


int main(){

    int n;
    cout<<"enter the desired number";
    cin>>n;

    int i=1;
    int sum=0;

    while(i<=n){
        sum=sum+i;
        i=i+1;
    }
    cout<<"sum from 1 to desired entered(n) is"<<sum<<endl;
}