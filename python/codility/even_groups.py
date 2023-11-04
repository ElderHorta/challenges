"""Creates a function, split_integer(), that takes two integers as inputs, a and b. The integer a needs to be split 
into b groups as evenly as possible"""


def split_integer(a, b):
    if b <= 0 or a <= 0:
        raise ValueError('Please, provide values higher than zero.')
    
    division = a // b
    remainder = a % b

    group = []
    for _ in range(b):

        if remainder > 0:
            group.append(division + 1)
            remainder -= 1
        else:
            group.append(division)
        
    print('The most evenly list possible is:', group)

split_integer(50, 4)
