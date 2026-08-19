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

    # N X N 배열
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

        moving_horse_index_array = []

        for i in range(len(current_stacked_horse_map[r][c])):
            current_stacked_horse_index = current_stacked_horse_map[r][c][i]
            # 여기서 이동해야 하는 애들은 현재 옮기는 말 위의!!! 말들이다.
            if horse_index == current_stacked_horse_index:
                moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                break

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