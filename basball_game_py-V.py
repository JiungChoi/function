import random

def generate_numbers():
    numbers = []
    
    while(1):
        pre_in = random.randint(1,9)
        if pre_in not in numbers:
            numbers.append(pre_in)
        if (len(numbers) == 3):
            print(numbers)
            return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    
    i=0
    while(i!=3):
        pre_in = input(f"{i+1}번째 숫자를 입력하세요: ")
        error =check_error(pre_in, new_guess)
        if error == 0 :
            new_guess.append(int(pre_in))
            i += 1
        elif error == 1:
            continue
        
    return new_guess

def check_error(pre_in, new_guess):
    if(int(pre_in) in new_guess):
        print("중복되는 숫자입니다. 다시 입력하세요.")
        return 1
    elif((int(pre_in) <= 0) or (int(pre_in) > 9)):
        print("범위를 벗어나는 숫자입니다. 다시 입력하세요. ")
        return 1
    return 0

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(0,3):
        if(guess[i]==solution[i]):
            strike_count += 1
        else:
            if(guess[i] in solution):
                ball_count += 1

    return strike_count, ball_count

answer = generate_numbers()
tries = 1
while(1):
    s1, b1= get_score(answer,take_guess())
    print(f"strike : {s1}, ball: {b1}")
    
    if(s1 == 3):
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
        break
    
    tries += 1
  

