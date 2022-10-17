#include <iostream>
using namespace std;

 
int main(){
  	float ganancias, donativo;
  	cout<<"Ingrese las ganancias del ultimo mes: ";cin>> ganancias;
  	while(ganancias<0){
  		cout<<"Digite un numero valido: ";cin>> ganancias;
	  }
  	
  	if(ganancias>=0 && ganancias<=1000){
  		donativo=ganancias*0.05;
	  }
	if(ganancias>1000 && ganancias<=1500){
		donativo=ganancias*0.07;
	}
	if(ganancias>1500 && ganancias<=2000){
		donativo=ganancias*0.08;
	}
	if(ganancias>2000 && ganancias<=5000){
		donativo=ganancias*0.1;
	}
	if(ganancias>5000){
		donativo=ganancias*0.15;
	}
  	
  	cout<<"\nEl donativo segun la ultima ganancia es: "<<donativo;
  	
  	return 0;
}
