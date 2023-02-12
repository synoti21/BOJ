#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    long long int sum1 = 0, sum2 = 0;
    deque<int> dq1;
    deque<int> dq2;


    int count=0;
    for_each(queue1.begin(), queue1.end(), [&](int& n){
        dq1.push_back(n);
        sum1+=n;
       });
    for_each(queue2.begin(), queue2.end(), [&](int& n){
        dq2.push_back(n);
        sum2+=n;
    });
    int fail = queue1.size() * 3;
    while(1){
        if(count > fail){
            return -1;
        }

        if(sum1 > sum2){
           int temp = dq1[0];
            dq1.pop_front();
            dq2.push_back(temp);
            sum1-=temp;
            sum2+=temp;
            count++;
        }else if(sum1 < sum2){
            int temp = dq2[0];
            dq2.pop_front();
            dq1.push_back(temp);
            sum1+=temp;
            sum2-=temp;
            count++;
        }else{
            return count;
        }

    }
}