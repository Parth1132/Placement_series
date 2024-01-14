#include<iostream>
using namespace std;

int main () {

    int amt;
    cout<<"enter the amt to be broken:"<<endl;
    cin>>amt;

    int n100,n50,n10,n1;
    n100=n50=n10=n1=0;

    switch(amt>=100)
    {
        case 1:n100=amt/100;
        amt -= n100*100;
        break;
    }

    switch(amt>=50)
    {
        case 2: n50=amt/50;
        amt -= n50*50;
        break;
    }
    switch(amt>=10)
    {
        case 1: n10=amt/10;
        amt -= n10*10;
        break;
    }
    switch(amt>=1)
    {
        case 1: n1=amt/1;
        amt -= n1*1;
        break;
    }

    cout<<"n100 ="<<n100<<endl;
    cout<<"n50 ="<<n50<<endl;
    cout<<"n10 ="<<n10<<endl;
    cout<<"n1 ="<<n1<<endl;




}