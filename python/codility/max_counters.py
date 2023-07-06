'''
create a function solution(n,a), where n is an integer bigger than 0 that will represent the size of a list
and a is a non-empty integer list that contain numbers > 0.
Example: n = 3, a = [1,2,1,4,3,2,4,1]
You should create a new list with size n and only 0 values, new_list = [0,0,0,0,0]
'''
import os
os.system('cls')

def solution(n, a):
    list_size = n
    commands = a
    list = [0] * list_size
    max_counter = 0

    for i in commands:
        if i <= list_size:
            list[i-1] += 1
            print(list)
            if max_counter < list[i-1]:
                max_counter = list[i-1]
        else:
            print('Setting all the list equals to the max counter value', max_counter)
            list = [max_counter] * n 
            print(list)

    return list

a = [3,4,4,6,1,4,4]
n = 5
print('Solution is:', solution(n, a))
