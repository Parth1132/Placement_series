#include<iostream>
using namespace std;

int main () {

    int n;
    cout<<"enter the number to be checked";
    cin>>n;

    bool isprime=1;

    for(int i=2;i<n;i++){

        if(n%i==0)
        {
        isprime=0;
        break;

        }

    }
    if(isprime==0){
        cout<<"the entered number is not a prime number";

    }
    else{
        cout<<"the entered number is a prime number";
    }





}