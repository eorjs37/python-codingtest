def find_max_occurred_alphabet(string):
    arr = [0]*26

    for char in string:
        if(char.isalpha() == False):
            continue
        index = ord(char)-97
        arr[index] += 1

    max_index= arr.index(max(arr))
    return chr(max_index+97)
# 1 abc처럼 

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
