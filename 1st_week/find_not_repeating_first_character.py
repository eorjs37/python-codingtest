def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    alp_array = [0] * 26

    for char in string:
        alp_array[ord(char)-97]+=1

    not_repeating_char_array = []
    for index in range(len(alp_array)):
        alphabet_occurrence = alp_array[index]
        if alphabet_occurrence == 1:
            not_repeating_char_array.append(chr(index+ord('a')))

    for char in string:
        if char in not_repeating_char_array:
            return char
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))