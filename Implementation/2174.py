#로봇은 복수개이며
#명령어가 순서대로 움직이므로, 각 명령어가 실행될 때마다 단 한개의 로봇이 한 번의 동작을 한다.
#이를 반복함

#충돌이 일어나면 즉시 break하고 결과를 출력하면 될 듯
#만일 break되지 않고 모두 명령어 수행을 끝내면 OK

#필요한 변수는 로봇 배열 (로봇 번호, x, y, 로봇 방향) , 명령어 배열 (명령 대상, 명령어 종류, 반복 횟수)
#함수는 command 함수 (명령 실행), execute (행동 실행)
#for문으로 명령어 배열을 탐색한 후, 종류, 횟수를 읽어 반복문
#그래프를 만들어야 충돌이나 범위 밖을 표현할 때 더 유용.
#0은 아무것도 없을 때, 그리고 각 숫자는 로봇의 번호를 의미

#오답이었던 이유: 로봇이 지나가면 그 자리는 빈공간 이므로 -1로 복귀시켜야 한다.

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[-1 for _ in range(a)] for _ in range(b)]
robot = []
cmd = []

direct = ['N','E','S','W']

for i in range(n):
    x,y,dir = map(str,input().split())   #5 ,4  (1,1)
    dir_num = 0
    for j in range(len(direct)):
        if direct[j] == dir:
            dir_num = j

    x_i = int(x)
    y_i = b-int(y)
    robot.append([i,x_i-1,y_i,dir_num])
    graph[y_i][x_i-1] = i

for i in range(m):
    num, com, rep = map(str,input().split())
    cmd.append((int(num)-1, com, int(rep)))

def command():
    for i in range(len(cmd)):
        exec(i)
    print("OK")


def exec(comm_n):
    global graph, robot
    robot_num, comm, rep = cmd[comm_n]
    robot_x = robot[robot_num][1]
    robot_y = robot[robot_num][2]
    if comm == 'L':
        for i in range(rep):
            robot[robot_num][3] -= 1
            if robot[robot_num][3] < 0:
                robot[robot_num][3] = 3
    elif comm == 'R':
        for i in range(rep):
            robot[robot_num][3] = (robot[robot_num][3]+1)%4

    elif comm == 'F':
        robot_dir = robot[robot_num][3]
        o_robot_x = robot[robot_num][1] #원래대로 복원
        o_robot_y = robot[robot_num][2] #원래대로 복원
        if robot_dir == 0: #N
            for i in range(rep):
                robot_y -=1
                if robot_y < 0:
                    print("Robot " + str(robot_num+1) + " crashes into the wall")
                    exit()
                elif graph[robot_y][robot_x] != -1:
                    print("Robot " + str(robot_num+1) + " crashes into robot "+str(graph[robot_y][robot_x]+1))
                    exit()
            robot[robot_num][2] = robot_y
            graph[robot_y][robot_x] = robot_num
            graph[o_robot_y][o_robot_x] = -1 #오답의 폐인
        elif robot_dir == 1: #E
            for i in range(rep):
                robot_x+=1
                if robot_x >= a:
                    print("Robot " + str(robot_num+1) + " crashes into the wall")
                    exit()
                elif graph[robot_y][robot_x] != -1:
                    print("Robot " + str(robot_num+1) + " crashes into robot "+str(graph[robot_y][robot_x]+1))
                    exit()
            robot[robot_num][1] = robot_x
            graph[robot_y][robot_x] = robot_num
            graph[o_robot_y][o_robot_x] = -1
        elif robot_dir == 2: #S
            for i in range(rep):
                robot_y += 1
                if robot_y >= b:
                    print("Robot " + str(robot_num+1) + " crashes into the wall")
                    exit()
                elif graph[robot_y][robot_x] != -1:
                    print("Robot " + str(robot_num+1) + " crashes into robot "+str(graph[robot_y][robot_x]+1))
                    exit()
            robot[robot_num][2] = robot_y
            graph[robot_y][robot_x] = robot_num
            graph[o_robot_y][o_robot_x] = -1
        elif robot_dir == 3: #W
            for i in range(rep):
                robot_x -= 1
                if robot_x < 0:
                    print("Robot " + str(robot_num+1) + " crashes into the wall")
                    exit()
                elif graph[robot_y][robot_x] != -1:
                    print("Robot " + str(robot_num+1) + " crashes into robot "+str(graph[robot_y][robot_x]+1))
                    exit()
            robot[robot_num][1] = robot_x
            graph[robot_y][robot_x] = robot_num
            graph[o_robot_y][o_robot_x] = -1

command()



