#include <bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm,"BGI");
    
    setcolor(GREEN);
    
    rectangle(50,50,200,150);
    rectangle(100,100,250,200);
    
    line(50,150,100,200);
    line(50,50,100,100);
    line(200,150,250,200);
    line(200,50,250,100);
    
    outtextxy(170,230,"CUBE"); //assign text
    
    getchar();
    return 0;
}


