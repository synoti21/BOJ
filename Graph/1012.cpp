#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void bfs(int x, int y){
    queue<pair<int,int>> deque;
    pair<int,int> =

    while(deque.empty()){
        pair<int,int> p;
        p = deque.front();


    }
}

void sol(){
    int m,n,k;
    int cnt = 0;

    cin >> m >> n >> k;

    int graph[50][50];
    int visited[50][50];
    memset(graph, 0, sizeof(graph));
    memset(visited, 0, sizeof(visited));


    for (int i =0 ; i < k ; i++){
        int x,y;
        cin >> x >> y;
        graph[y][x] = 1;
    }

    for (int i =0 ; i < n ; i++){
        for (int j= 0 ; i< m ; j++){
            if(graph[i][j] == 1 && visited[i][j] == 0)
                bfs(j,i);
                cnt+=1;
        }
    }

}
int main(void){
    int T;
    cin >> T;

    for (int i =0; i< T ; i++){
        sol();
    }
}