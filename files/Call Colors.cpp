#include<iostream>
#include<conio.h>
#include<stdlib.h>

using namespace std;

void color(){
    system("color 02");
}

void calout(){
    char name[] = "";
    cout << "Enter your name: ";
    cin >> name;
    
}

void main(){
    color();
    calout();
    cout << "Hacked!";
    getch();

}
