
import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE


#方向坐标
move = {'0': [0, 1],
        '1': [1, 1],
        '2': [1, 0],
        '3': [1, -1],
        '4': [0, -1],
        '5': [-1, -1],
        '6': [-1, 0],
        '7': [-1, 1]}
#反转数，满足从右到左的要求
number = ('0' * nb_of_leading_zeroes + f'{int(code):o}')
number = number[::-1]
#print(number)

start = [[0, 0]]
temp = []
loc = [(0, 0)]
path = []
x_move = 0
y_move = 0

#find white 棋子
for i in number:
    x, y = move[i]
    x_move = x_move + x
    y_move = y_move + y
    temp = (x_move,y_move)
   # print(temp)

    if (temp) in loc:
        loc.remove(temp)
    else:
        loc.append(temp)


loc =  [(0, 0)] + loc
print(loc)

x_max = -1
for i in loc:
    x , y = i
    if x_max > x:
       x_max = x_max
    else:
        x_max = x
print(x_max)

x_min = 0
for i in loc:
    x , y = i
    if x_min < x:
        x_min = x_min
    else:
        x_min = x
print(x_min)

y_min = 0
for i in loc:
    x , y = i
    if y_min < y:
        y_min = y_min
    else:
        y_min = y
print(y_min)

y_max = -1
for i in loc:
    x , y = i
    if y_max >y:
        y_max = y_max
    else:
        y_max = y
#print(y_max)
#输出

for y in range(y_max, y_min - 1, -1):
    for x in range(x_min, x_max + 1, 1):
        if (x, y) in loc:
           print(on, end="")
        else:
           print(off, end='')
    if y_min < y:
        print()


