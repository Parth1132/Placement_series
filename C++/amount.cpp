#include<iostream>
using namespace std;


int main() {

    int amount;
    cout<<"enter the desired amt:"<<endl;
    cin>>amount;

    int n500,n100=0,n50=0,n20,n10=0;

   switch(amount>=500)
	{
		case 1:
			n500 = amount/500;
        	amount -= n500 * 500;
        break;
	}
	switch(amount >=100)
	{
		case 1:
			n100 = amount/100;
        	amount -= n100 * 100;
        break;
	}
	switch(amount >=50)
	{
		case 1:
			n50 = amount/50;
        	amount -= n50 * 50;
	}
	switch(amount >=20)
	{
		case 1:
			n20 = amount/20;
        	amount -= n20 * 20;
        break;
	}
	switch(amount >=10)
	{
		case 1:
			n10 = amount/10;
        	amount -= n10 * 10;
        break;
	}
    cout << "500 = " << n500 <<endl;
    cout << "100 = " << n100 <<endl;
    cout << "50 = " << n50 <<endl;
    cout << "10 = " << n10 <<endl;

}