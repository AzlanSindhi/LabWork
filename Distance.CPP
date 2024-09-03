#include<iostream.h>
#include<conio.h>

class Distance{
	private:
		int meters, kilometers;
	public:
		Distance(int km = 0, int m = 0):kilometers(km),meters(m){}

		friend Distance TotDis(const Distance &d1, const Distance &d2);

		void getData(){
			cout << "Enter Meters: ";
			cin >> meters;
			cout << "Enter Kilometers: ";
			cin >> kilometers;
		}
		void Display(){

		cout << "Distance: " << kilometers << " Kilometers," << meters << " meters" << endl;


		}

};

Distance TotDis(const Distance &d1, const Distance &d2){

	int totalMeters = d1.meters + d2.meters;
	int totalKilometers = d1.kilometers + d2.kilometers +(totalMeters /1000);
	totalMeters = totalMeters % 1000;

	return Distance(totalKilometers, totalMeters);
}
int main(){

	Distance d1,d2;

	d1.getData();
	d2.getData();
	clrscr();
	Distance d3 = TotDis(d1,d2);
	cout << "Distance 1: ";
	d1.Display();
	cout << "Distance 2: ";
	d2.Display();
	cout << "Total Distance: ";
	d3.Display();


getch();
return 0;
}