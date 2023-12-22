#include<iostream>
using namespace std;


int main (){

    char ch;
    cout<<"enter the desired character"<<endl;

    cin>>ch;

    if(ch>=65 && ch<=90){
        cout<<ch<<"is an uppercase letter";
    }

    else if (ch>=97 && ch<=122){
        cout<<ch<<"is an lowercase letter";
    }
    else
    {
        cout<<ch<<"is not a alphabet it might be a digit";
    }

    return 0;
}