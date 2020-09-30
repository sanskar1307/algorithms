#include<iostream>
using namespace std;


int C(int n,int r)
{
    if(n==r||r==0)
    return 1;
    
    return C(n-1,r-1)+C(n-1,r);
}

int main(){
    int n,r;
    cin>>n>>r;
    cout<<C(n,r)<<endl;
    
}