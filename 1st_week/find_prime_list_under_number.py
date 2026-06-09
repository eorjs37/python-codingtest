input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    i = 2
    result = []
    while(i < number):
        # 1부터 시작해서 i까지 나눴을때 0이 나오면 count를 증가시킨다
        counter = 0
        is_prime = True
        for index in range(1,i+1):
            if(i % index == 0):
                counter +=1
            if(counter > 2):
                is_prime = False
                break

        if(is_prime):
            print(i)
            result.append(i)
        i = i+1


    print(result)
    return []


result = find_prime_list_under_number(input)
print(result)