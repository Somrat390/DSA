#include<bits/stdc++.h>
using namespace std;

string convert2binary(int n){
    string s = "";
    while(n!=0){
        s += (n % 2 == 1)? '1': '0';
        n = n / 2;
    }
    reverse(s.begin(), s.end());
    return s;  

}

int main(){
   int n;
   cin >> n;
   cout << convert2binary(n)<< endl;
}