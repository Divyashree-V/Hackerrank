#include <iostream>
#include <vector>
#include <string>

using namespace std;

template<class T>
void printArray(vector<T> v) 
{
    for(int i=0;i<v.size();i++) 
    {
        cout<<v[i]<<endl;
    }
} 
