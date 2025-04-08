test_num = int(input())
s_dict = {'}':'{', ')':'(',']':'['}
for i in range(test_num):
    flag = True
    n_list = input()
    s = []
    for i in n_list:
        if i in ['[', '{', '(']:
            s.append(i)
        else:
            if len(s) == 0: # 닫는 괄호는 오는데 여는 괄호가 없을경우
                flag = False 
                break
            else:
                if s.pop() != s_dict.get(i): # 닫는 괄호와 마지막 여는 괄호가 다를 경우
                    flag = False
                    break
                    
    if len(s) != 0: # 안닫힌 괄호가 있을 경우
        flag = False
    if flag:
        print('YES')
    else:
        print('NO')

                
                
            
            