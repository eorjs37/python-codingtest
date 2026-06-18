numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []

def dp(val,index,sum):
    return  1
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways(array,curent_index,current_sum):
        if curent_index == len(array):
            all_ways.append(current_sum)
            return
        get_all_ways(array,curent_index+1, current_sum + array[curent_index])
        get_all_ways(array, curent_index + 1, current_sum - array[curent_index])

    get_all_ways(array,0,0)
    print(all_ways)

    target_count = 0;

    for way in all_ways:
        if target == way:
            target_count +=1

    return  target_count
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))