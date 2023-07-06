'''You are given a non-empty list A of integers. The goal is to find the maximum absolute difference between any two elements in A. Write a function solution that 
takes a list of integers as input and returns the maximum absolute difference.

For example, given the list A = [2, 6, 8, 3], the function should return 6 because the maximum absolute difference is achieved by subtracting 2 from 
8 (i.e., 8 - 2 = 6).

Assume that:
The list A contains at least two elements.
Each element in A is an integer within the range [-1,000,000, 1,000,000].
Your solution should have linear time complexity.

For example, given the list A = [2, 6, 8, 3], the function should return 6.
'''

def solution(A):

    list = A
    max_num = -1000000
    min_num = 1000000

    for num in list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print('Min number is', min_num)
    print('Max number is', max_num)

    absolute_difference = abs(max_num - min_num)
    print('Maximum absolute difference is', absolute_difference)

    return absolute_difference

list = [2, 6, 8 , 3]
solution(list)
