from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 방향
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def get_d_index_when_to_left(d):
    return (d+1) % 4

def get_d_index_when_to_back(d):
    return (d+2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map=[[]],count = 0):
    # 모든방향을 탐색한다 BFS
    m = len(room_map) # 가
    n = len(room_map[0])
    count_of_departments_cleaned = 1  # 청소하는 칸의 개수
    # 청소 완료
    room_map[r][c] = 2
    # r,c,방향
    queue = deque([
        [r,c,d]
    ])

    while queue:
        r,c,d = queue.popleft()
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_to_left(temp_d)
            mr,mc = r+dr[temp_d],c+dc[temp_d]

            #
            if 0<= mr < m and 0<= mc < n and room_map[mr][mc] == 0:
                count_of_departments_cleaned += 1
                room_map[mr][mc] = 2
                queue.append([mr,mc,temp_d])
                break # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다. 1번이 현재위치청소 하고 다시 탐색한다
            elif i == 3:
              mr,mc = r + dr[get_d_index_when_to_back(d)], c + dc[get_d_index_when_to_back(d)]
              queue.append([mr,mc,d])

              if room_map[mr][mc] == 1:
                  return count_of_departments_cleaned

    return


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map,0))