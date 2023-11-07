'''In a randomly sorted list of integers from 1 to 5, 
find the minimum index where all the possible numbers (1 to 5) has already previously appeared
example of list = [3,2,1,3,1,4,2,3,5,4,4,1,2], in this case the index searched is 8.
'''
def solution(A):
    list = A
    counter = 0
    numbers_found = []

    for i in list:
        if i not in numbers_found:
            numbers_found.append(i)
            
            if len(numbers_found) == 5:
                print('The minimum index is', counter)
                break
        counter = counter + 1

    return counter


A = [3,2,1,3,1,4,2,3,5,4,4,1,2]
solution(A)
