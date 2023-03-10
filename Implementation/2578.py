row = [[0 for _ in range(5)] for _ in range(5)]
col = [[0 for _ in range(5)] for _ in range(5)]
diag = [0,0,0,0,0]
diag_t = [0,0,0,0,0]

game = [[1 for _ in range(5)] for _ in range(5)]
game_dic = {}
target = [[1 for _ in range(5)] for _ in range(5)]


for i in range(5):
    game[i] = list(map(int, input().split()))

for i in range(5):
    for j in range(5):
        game_dic[game[i][j]] = (i,j)

for i in range(5):
    target[i] = list(map(int, input().split()))

cnt = 0
bingo = 0
for i in range(5):
    for j in range(5):
        if bingo >= 3:
            break

        t_row = game_dic[target[i][j]][0]
        t_col = game_dic[target[i][j]][1]
        row[t_row].pop(0)
        col[t_col].pop(0)

        if t_row == 2 and t_col ==2:
            diag.pop(0)
            diag_t.pop(0)
            if len(diag) == 0:
                bingo+=1
            if len(diag_t) == 0:
                bingo+=1
        elif t_row == t_col:
            diag.pop(0)
            if len(diag) == 0:
                bingo+=1
        elif abs(2-t_row) == abs(2-t_col):
            diag_t.pop(0)
            if len(diag_t) == 0:
                bingo+=1
        if len(row[t_row]) == 0:
            bingo += 1
        if len(col[t_col]) == 0:
            bingo += 1
        cnt+=1

print(cnt)
