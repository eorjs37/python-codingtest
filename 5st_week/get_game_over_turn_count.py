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


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions = []):

    # 가로
    width = len(game_map)
    # 세로
    height = len(game_map[0])

    # 각 칸에 배열을 만든다.
    # 각 칸에 말이 쌓이면 말번호/행/열/이동방향
    visited =[]
    for i in range(len(game_map)):
        visited.append([])
        for sub_index in range(len(game_map[i])):
            visited[i].append([])


    # 깊이? 너비? 우선탐색
    # 최대 1000판
    # for i in range(0,1000):
    #     print(i)

    # horse_location_and_directions 만큼 반복한다
    # 행, 열의 인덱스, 이동 방향
    # 이동 방향은 0, 1, 2, 3 이고 0부터 순서대로 →, ←, ↑, ↓
    # 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.

    # 1턴
    for item in horse_location_and_directions:
        row,col,direction = item
        mr = row + dr[direction]
        mc = col + dc[direction]


        if mr >= width or mc >= height or mr<0 or mc<0:
            continue

        space = game_map[mr][mc]

        if space == 0:
            visited[mr][mc].append([mr,mc,direction])
            print("하얀색")
        elif space == 1:
            print("빨간색")
        else:
            print("파란색")

    print(visited)
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