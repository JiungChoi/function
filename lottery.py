import random

def generate_numbers(n):
    nums = []

    while(1):
        pre_in = random.randint(1,45)
        if pre_in not in nums:
            nums.append(pre_in)
        if len(nums) == n:
            break
    return nums

def draw_winning_numbers():
    return generate_numbers(6) + generate_numbers(1)

def count_matching_numbers(rotto_list, customer_list):
    cnt = 0
    for comp in customer_list:
        if comp in rotto_list:
            cnt += 1
    return cnt

def check(winning_numbers, numbers):
    result_org = count_matching_numbers(winning_numbers[0:len(winning_numbers)-1], numbers)
    result_bonus = winning_numbers[len(winning_numbers)-1]

    result = 0
    if result_org == 6:
        result= 1000000000
    elif result_org == 5:
        if result_bonus in numbers:
            result= 50000000
        else :
            result= 1000000
    elif result_org == 4:
        result= 50000
    elif result_org == 3:
        result= 5000

    return result
