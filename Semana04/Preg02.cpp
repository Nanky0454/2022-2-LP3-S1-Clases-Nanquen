//Dado n, hallar la suma de los n primeros n�meros naturales//
#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	float suma, n;
	n = 0;
	
	cout<<"El valor de n: ";
	
	cin>>n;
	suma = n*(n+1)/2;
	
	cout<<"Sumatoria = "<<suma;
	
	return 0;
}

