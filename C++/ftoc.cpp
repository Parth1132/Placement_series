#include<iostream>
using namespace std;

int main() {
    double fahrenheit, celsius;
    cout<<"enter the temp in fahrenheit";
    cin>>fahrenheit;

    celsius=(fahrenheit-32)*5.0/9.0;

    cout<<"temp in celsius is"<<" "<<celsius<<endl;
}