input = "abcabcabcabcdededededede"

# aabbaccc
# a a b b a c c c => 2a2ba3c

# ababcdcdababcdcd
# ab ab cd cd ab ab cd cd => 2ab2cd2ab2cd
# ababcdcd ababcdcd => 2ababcdcd

# abcabcdede
# abc abc dede => 2abcdede

# abcabcabcabcdededededede
# abc abc abc abc ded ede ded ede => 4abcdededededede
# abcabc abcabc dedede dedede => 2abcabc2dedede

# xababcdcdababcdcd => 17

# jaaa => j3a

# AZAAAZDWAAA
# A Z A A A Z D W A A A => AZ3AZDW3A

# BBAABAAADABBBD
# B B A A B A A A D A B B B D => 2B2AB3ADA3BD

def string_compression(string =''):
    N = len(string)//2
    index = 0
    while index<len(string):
        print(string[index:index+3])
        index+=3

    # for i in range(1,N+1):
    #     print(i)

    return


print(string_compression(input))  # 14 가 출력되어야 합니다!

# print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
# print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
# print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))