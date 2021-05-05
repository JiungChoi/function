import random

dic = {

}

while (1):
    pre_in = input('영어 단어를 입력하세요:')
    
    if pre_in == 'q':
        break
    elif pre_in in dic.keys():
        print('이미 들어있는 단어네요.')
        continue
    
    dic[pre_in] = input('한국어를 입력하세요:')

print(dic)

while(1):
    print("<< 영어 단어 퀴즈입니다 >>")

    key_ran = list(dic.keys())
    random.shuffle(key_ran)

    for key in key_ran:
        ask = dic[key]
        
        answer = input(f'{ask}:')
        if(answer == ask):
            print("오우 정답!")    
    keep_go = input('계속 하시겠나요? (y or n)')
    if(keep_go == 'n'):
        break

    
