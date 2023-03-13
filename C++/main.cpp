#include <iostream>
#include <algorithm>
#include <queue>
#define INF 100
using namespace std;

int n;
int graph[125][125];
int table[125][125];


int dijkstra(){
    int nr[4] = {1,-1,0,0};
    int nc[4] = {0,0,1,-1};

    int now_wei, n_row, n_col, new_wei;

    priority_queue<pair<int,pair<int,int>>> pq;
    pq.push(make_pair(graph[0][0], make_pair(0,0)));

    while(!pq.empty()){
        pair<int,pair<int,int>> n_node_pair = pq.top();
        pq.pop();
        now_wei = n_node_pair.first;

        n_row = n_node_pair.second.first;
        n_col = n_node_pair.second.second;

        for(int i = 0 ;i < 4; i++){
            int dr = n_row + nr[i];
            int dc = n_col + nc[i];

            if(0 <= dr < n && 0 <= dc < n){
                new_wei = now_wei + graph[dr][dc];
                if(table[dr][dc] > new_wei){
                    table[dr][dc] = new_wei;
                    pq.push(make_pair(new_wei, make_pair(n_row,n_col)));
                }
            }
        }
    }
    return table[n-1][n-1];

}

int main(void){
    int problem_cnt = 1;
    while(true){
        memset(table, 100, sizeof(table));
        cin >> n;
        if(!n){
            return 0;
        }
        for(int i =0 ;i < n; i++){
            for(int j = 0; j <n ; j++){
                cin >> graph[i][j];
            }
        }
        cout << "Problem " << problem_cnt << ": " << dijkstra() << endl;
        problem_cnt++;
    }
}