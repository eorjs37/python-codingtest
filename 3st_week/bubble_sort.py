input = [4, 6, 2, 9, 1]

# 0 1 2 3 4
# 4 6 2 9 1

# 1회전(1~5번째까지 비교)
# i=0,j=5-0-1
# range(4)
# if array[0] > array[0+1]
# array[0+1],array[0] = array[0],array[0+1]
# 4 6 2 9 1
# 4 2 6 1 9

# 2회전(1~4번째까지 비교)
# i=0,j=5-1-1
# 4 2 6 1 9
# 2 4 1 6 9

# 3회전 (1~3번째까지 비교)
# 2 4 1 6 9
# 2 1 4 6 9

# 4회전 (1~2번째까지 비교)
# 2 1 4 6 9
# 1 2 4 6 9
def bubble_sort(array):
    n = len(array)
    for i in range(n-1): # 4
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))