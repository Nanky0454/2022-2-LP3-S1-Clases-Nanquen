#include<iostream>
using namespace std;
int main(){
	int horas=0;
	int costo;
	cout<<"Ingresar el numero de horas en la playa\n";
	cin>>horas;

if(horas<=4){
	costo=6;
	cout<<"Monto a pagar\n";
	cout<<costo; 
}
if(horas>4){
		costo=((horas-4)*2)+6;
		cout<<"Monto a pagar\n";
		cout<<costo;
}
}

