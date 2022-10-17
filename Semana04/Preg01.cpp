#include <iostream>
using namespace std;

 
int main(){
	float a,b,aux;
	cout<<"Ingrese el numero a: ";cin>>a;
	cout<<"Ingrese el numero b: ";cin>>b;
	
	aux=a;
	a=b;
	b=aux;
	
	cout<<"\nLos nuevos valores son: ";
	cout<<"\nA: "<<a;
	cout<<"\nB: "<<b;
	
	return 0;
	
}
