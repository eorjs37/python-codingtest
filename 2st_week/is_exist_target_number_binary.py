finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    # 이 부분을 채워보세요!
    sorted_array = sorted(array)
    current_min = 0
    current_max = len(sorted_array) - 1
    current_guess = (current_max + current_min) // 2

    while current_min <= current_max:
        if sorted_array[current_guess] == target:
            return True
        elif sorted_array[current_guess] < target:
            current_min = current_guess + 1
        elif sorted_array[current_guess] > target:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)