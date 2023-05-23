# COMP9021 22T3
# Quiz 5 *** Due Friday Week 8 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Monday Week 9 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines moved to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines moved to the right by one position, e.g.
#      111
#       111
#        111
#         111
# The size is the number of 1s in the parallelogram. In the above examples, the size is 12.

from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)
        #print(grid[5][0])

def size_of_largest_parallelogram(left,right,vertical):

    return max(left,right,vertical)

#遍历，匹配，存数k，得数值，取最大。


def vertical(i, j, l):
        i = 2 #横坐标
        j = 0 #纵坐标
        i_old = i
        l = 0 #长度
        temp = [ ] #存储所有符合条件的数字
        while grid[i][j] == 1:
            l = l + 1
            j = j + 1
        while i in range(0,11) and j in range(0,11):
            for m  in grid[i][j-1:j-1+l]:
                temp.append(m)
            if not all(temp):
                break
            j = j -1
            i = i -1

        if i_old -i ==1:
            return 0
        return l*(i_old - i)


def left(i, j, l):
    i = 2  # 横坐标
    j = 0  # 纵坐标
    i_old = i
    l = 0  # 长度
    temp = []  # 存储所有符合条件的数字
    while grid[i][j] == 1:
        l = l + 1
        j = j + 1
    while i in range(0, 11) and j in range(0, 11):
        for m in grid[i][j - 1:j - 1 + l]:
            temp.append(m)
        if not all(temp):
            break
        j = j - 1
        i = i - 1

    if i_old - i == 1:
        return 0
    return l * (i_old - i)

def right(i, j, l):
        i = 2  # 横坐标
        j = 0  # 纵坐标
        i_old = i
        l = 0  # 长度
        temp = []  # 存储所有符合条件的数字
        while grid[i][j] == 1:
            l = l + 1
            j = j + 1
        while i in range(0, 11) and j in range(0, 11):
            for m in grid[i][j - 1:j - 1 + l]:
                temp.append(m)
            if not all(temp):
                break
            j = j - 1
            i = i - 1

        if i_old - i == 1:
            return 0
        return l * (i_old - i)



try:

    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                               ).split()
                         )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')