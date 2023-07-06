'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2, 147, 483, 648.. 2, 147, 483, 647].
'''

import os
os.system('cls')

def solution(A):
    mid_lenght = len(A) / 2
    sorted_list = sorted(A)
    current_counter = 1
    max_counter = 0
    previous_num = -2147483649
    dominator = 2147483649
    index = -1

    for num in sorted_list:
        current_counter = current_counter + 1

        if num != previous_num:
            current_counter = 1

        if current_counter > max_counter:
            max_counter = current_counter
            dominator = num
            print('max counter:', max_counter)
            print('dominator is:', dominator)

        previous_num = num
        print('mid lenght is:', mid_lenght)

    if (dominator != 2147483649) and (max_counter > mid_lenght): 
        for i in A:
            index += 1
            if i == dominator:
                break

    return index


A = [4, 3, 3, 2, 3, -1, 3, 1, 3]
print(type(A))
print('Solution is:', solution(A))

