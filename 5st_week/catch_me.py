from collections import deque

c = 11
b = 2

def tree(start,depth):
    operation = [['minus',1],['add',1],['multiply',2]]

    treeMap = {depth:[start]}
    depth+=1


    while depth<=5:
        prev_depth = depth-1
        treeMap[depth] = []
        for item in treeMap[prev_depth]:
            operand = item
            for i in range(len(operation)):
                [op,num] = operation[i]
                match op:
                    case 'minus':
                        treeMap[depth].append(operand - num)
                    case 'add':
                        treeMap[depth].append(operand + num)
                    case 'multiply':
                        treeMap[depth].append(operand * num)
        depth+=1

    return treeMap

def catch_me(cony_loc, brown_loc):
    # 브라운 위치를 b-1,b+1,b*2 으로 깊이너비 탐색한다
    tree(brown_loc,0)

    # 코니를 움직여보자
    return


print(catch_me(c, b))  # 5가 나와야 합니다!

# print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
# print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
# print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))