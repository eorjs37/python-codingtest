def is_correct_parenthesis(string):
    str = list(string)
    stack = []
    result = True

    for index in range(len(str)):
        if str[index] == "(":
            stack.append(str[index])
        else:
            if len(stack) == 0:
                result = False
                break
            else:
                if stack[len(stack)-1] == "(":
                    stack.pop()
                else:
                    result = False

    if len(stack) != 0:
        result = False

    return result


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))