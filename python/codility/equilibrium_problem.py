'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''

import os
os.system('cls')

def solution_1(A):
    lenght = len(A)
    iteration = lenght
    global_diff = 2000000

    while iteration > 1:
        left_sum = sum(A[0:lenght - iteration + 1])
        print('left is:', left_sum)
        right_sum = sum(A[lenght - iteration + 1:lenght])
        print('right is:', right_sum)
        diff = abs(left_sum - right_sum)
        print('diff is:', diff)
        if diff < global_diff:
            global_diff = diff
            print('global diff is:', global_diff)

        iteration = iteration -1

    return global_diff

def solution_1(A):
    lenght = len(A)
    global_diff = 2000000
    left_sum = 0
    total_sum = sum(A)

    for i in range(0, lenght):
        left_sum += A[i]
        diff=abs(2*left_sum - total_sum)
        global_diff = min(global_diff, diff)

    return global_diff

A = [1000,-1000]
print('solution_1 is:', solution_1(A)) #bad performance
print('solution_1 is:', solution_1(A)) #good performance
