from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0

    queue = deque()
    queue.append((brown_loc,time))
    visited = [{} for _ in range(200001)]
    # (위치:시간)으로 기억
    while queue and time<=200000:
        cony_loc+=time
        if time in visited[cony_loc]:
            return time

        for i in range(len(queue)):
            current_position,current_time = queue.popleft()

            next_time = current_time + 1

            next_position = current_position - 1
            # next_position에 시간이 없다면 추가
            if next_position<=200000 and next_time not in visited[next_position]:
                queue.append((next_position,next_time))
                visited[next_position].update({next_time:True})

            next_position = current_position + 1
            if next_position<=200000 and  next_time not in visited[next_position]:
                queue.append((next_position,next_time))
                visited[next_position].update({next_time: True})

            next_position = current_position * 2
            if next_position<=200000 and  next_time not in visited[next_position]:
                queue.append((next_position,next_time))
                visited[next_position].update({next_time: True})

        time += 1


    return


print(catch_me(c, b))

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))