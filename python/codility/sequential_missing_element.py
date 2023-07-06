'''In a sequential list, find the missing element.
For example, in liast = [1,2,3,4,5,7,8] the missing element is 6. 
Consider that each list have maximum one missing element.
'''
import os

os.system('cls')

def solution(A):

    list = A
    print('list is', list)
    
    for i in range(len(list)):

        number = int(list[i])
        next_number = int(list[i + 1])
        print('Number is', number, 'Next number is', next_number)

        if number == next_number - 1:
            continue
        else:
            missing_element = list[i] + 1
            break
    
    print('Missing element is', missing_element)
    return missing_element


A = [1,2,3,4,5,7,8]
solution(A)
