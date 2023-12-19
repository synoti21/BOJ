# 특별한 알고리즘은 없고 완전 탐색
# 그럼 백트래킹을 사용해서, 연주 곡이 늘어나면 이어서 탐색, 늘어난 곡이 없으면 백
import copy

answer = 100
s_count = 0


def dfs(depth, song_count, guitar_list, visited, song_list): #깊이, 필요한 기타 갯수, 기타 배열, 방문 여부, 칠 수 있는 곡 리스트
    global answer, s_count
    if song_count > s_count or (song_count >= s_count and answer > depth): #노래 갯수 최고 기록을 갱신했다면
        s_count = song_count
        answer = depth #답 새로 고침

    if depth == len(guitar_list): #그렇지 않고 끝에 도달했다면
        return

    for i in range(len(guitar_list)):
        count = 0 #새롭게 연주할 수 있는 곡 변수
        temp_list = copy.deepcopy(song_list) #새롭게 연주할 수 있는 곡
        for j in range(len(temp_list)):
            if temp_list[j] == 0 and guitar_list[i][j] == 1: #새로운 곡이 발견이 되면
                temp_list[j] = 1 #곡 리스트 새로고침
                count += 1
        if count > 0 and visited[i] == 0: #한 곡이라도 새로 칠 수 있고
            visited[i] = 1
            dfs(depth+1, song_count+count, guitar_list, visited, temp_list)
            visited[i] = 0
    return # 더 이상 탐색이 불가능하면 return

n, m = map(int, input().split())
guitar = [[] for _ in range(n)]
for i in range(n):
    guitar_type, song = map(str, input().split(' '))
    song = list(map(str, song.strip()))
    for j in range(m):
        song[j] = 0 if song[j] == 'N' else 1
    guitar[i] = song

dfs(0,0,guitar, [0 for _ in range(n)], [0 for _ in range(m)])
if s_count > 0:
    print(answer)
else:
    print(-1)