from collections import deque

balanced_parentheses_string = "()))((()"


# 올바른 문자열
def is_correct_parenthesis(string):
    queue = deque(string)
    stack = []
    while queue:
        pop = queue.popleft()
        if pop == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(queue) == 0:
        return False

    return True

def separate_parentheses(string):
    queue = deque(string)
    left_count,right_count = 0,0
    u,v = "",""

    while queue:
        pop = queue.popleft()
        if pop == "(":
            left_count+=1
            u+=pop
        else:
            u += pop
            right_count+=1

        if left_count == right_count:
            v = "".join(queue)
            return u,v

    return u,v

def change_to_parentheses(string):
    return

def get_correct_parentheses(string):

    return



# print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
#
# print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
# print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
# print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))