#include <iostream>
#include <algorithm>

using namespace std;

int n;
int graph[125][125];


int main(void){
    int problem_cnt = 1;

    while(true){
        cin >> n;
        if(cin){
            return 0;
        }
        for(int i =0 ;i < n; i++){
            for(int j = 0; j <n ; j++){
                cin >> graph[i][j];
            }
        }

        for (int i = 0 ;i < n ; i++) {
            for (int j = 0; j < n; j++) {
                cout << graph[i][j] << " ";
            }
            cout << endl;
        }
        problem_cnt++;

    }

}