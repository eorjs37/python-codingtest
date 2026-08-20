k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_de_index_when_go_back(d):
    if d % 2 == 0:
        return  d+1
    else:
        return d-1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions = []):
    n = len(game_map)

    turn_count = 1
    # horse_count: 말 개수
    # game_map : 게임맵
    # horse_location_and_directions: 말의 행/열/방향
    # current_stacked_horse_map: 위치마다 말을 stack으로 쌓는 형태
    # 동(0) -> 서(1) -> 북(2) -> 남(3)
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]

    # current_stacked_horse_map 에 위치시켜주기
    for i in range(len(horse_location_and_directions)):
        r,c,d = horse_location_and_directions[i]

        current_stacked_horse_map[r][c].append(i)

    # 1턴
    for horse_index in range(len(horse_location_and_directions)):
        r,c,d = horse_location_and_directions[horse_index]

        new_r = r + dr[d]
        new_c = c + dc[d]

        # 파란색의 경우
        if not 0 <= new_r <n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:

            continue

        moving_horse_index_array = []

        for i in range(len(current_stacked_horse_map[r][c])):
            current_stacked_horse_index = current_stacked_horse_map[r][c][i]
            if current_stacked_horse_index == horse_index:
                # 이동할려는 말들의 모음이다
                moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                break

        # 이동할려는 칸이 빨간색인 경우
        if game_map[new_r][new_c] == 1:
            moving_horse_index_array = reversed(moving_horse_index_array)

        for moving_horse_index in moving_horse_index_array:
            current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
            # 말 위치 업데이트
            horse_location_and_directions[moving_horse_index] = [new_r, new_c, d]
    while turn_count<=1000:
        turn_count+=1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

# start_horse_location_and_directions = [
#     [0, 1, 0],
#     [1, 1, 0],
#     [0, 2, 0],
#     [2, 2, 2]
# ]
# print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

# start_horse_location_and_directions = [
#     [0, 1, 0],
#     [0, 1, 1],
#     [0, 1, 0],
#     [2, 1, 2]
# ]
# print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))