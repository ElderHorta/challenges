'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''

import os
os.system('cls')

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = [A]
    odd_list = []
    paired_list = []

    for i in A:
        if i not in paired_list:
            odd_list.append(i)
            paired_list.append(i)
        else:
            try:
                odd_list.remove(i)
            except:
                pass
    try:
        odd_number = odd_list[0]
    except:
        odd_number = 0
    return odd_number


def solution_2(A):
    A = A
    occurrences = {}

    for num in A:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    for num, count in occurrences.items():
        if count % 2 != 0:
            return int(num)
        

def solution_3(A):
    A = [A]
    sorted_list = sorted(A)
    first_occurrence = True
    last_iteration = len(A)
    counter = 0
    odd = sorted_list[0]

    for i in sorted_list:
        if first_occurrence == True:
            first_occurrence = False
        elif (counter + 1 == last_iteration):
            odd = int(i)
            break
        else:
            if (sorted_list[counter-1]==i) or (sorted_list[counter+1]==i):
                pass
            else:
                odd = int(i)
                break
        counter += 1
    
    return odd


A = [9,3,9,3,9,7,9]
A = [42]

print('Solution is:', solution(A))      #bad performance
print('Solution 2 is:', solution_2(A))  #good performance
print('Solution 3 is:', solution_3(A))  #good performance

"""
Solution 2:
In this solution, we use a dictionary called occurrences to keep track of the count of each element in the array A. We iterate over each element in A 
and update the count in the occurrences dictionary accordingly.
After counting the occurrences of each element, we iterate over the items in the occurrences dictionary. We check if the count of an element is odd 
(count % 2 != 0). If we find such an element, we return it as the unpaired element.
"""
