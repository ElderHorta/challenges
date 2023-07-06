'''In a randomly sorted list, find the missing element.
For example, in list = [3,1,2,4,7,8,5] the missing element is 6. 
Consider that each list have maximum one missing element.
'''
import os
os.system('cls')

def solution(A):

    list = A
    print('list is', list)

    expected_list_lenght = len(list) + 1

    real_list_sum = sum(list)
    expected_list_sum = (expected_list_lenght * (expected_list_lenght + 1)) / 2 #formula to sum a sequential list of integers

    missing_element = int(expected_list_sum - real_list_sum)
    print('Missing element is', missing_element)

    return missing_element


A = [3,1,2,4,7,8,5]
solution(A)
