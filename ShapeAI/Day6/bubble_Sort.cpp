#include "iostream"
#include <bits/stdc++.h>

using namespace std; //standard namespace

void print(vector<int> vec){
    for (int x:vec) 
        cout<<x<<" ";
    
    cout<<"\n";    
}
void swap(int*a,int*b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void bubble_sort(vector<int> vec){
    for (int i = 0; i < vec.size(); i++)
    {
        for (int j = 0; j < vec.size()-i-1; j++)
        {
            if(vec[j]> vec[j+1]){
                swap(&vec[j],&vec[j+1]);
            }
        }
        
    }
    print(vec);
}

int main(void) 
{
    vector<int> vec = {11,43,2,3,55,33,88};
    print(vec);
    bubble_sort(vec); 
    return 0;
}