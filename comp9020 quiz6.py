
from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    global color,res
    res=grid
    color=1
    for i in range(dim):
        for j in range(dim):
            if(res[i][j]==1):
                color+=1
                dfs(i,j,color)
    return res
    # Replace pass above with your code


def max_number_of_spikes(nb_of_shapes):
    ans=[0 for i in range(color+1)]
    for i in range(dim):
        for j in range(dim):
            if(nb_of_shapes[i][j]!=0):
                tmp=0
                if(i>0 and nb_of_shapes[i-1][j]!=0):
                    tmp+=1
                if(j>0 and nb_of_shapes[i][j-1]!=0):
                    tmp+=1
                if(i<dim-1 and nb_of_shapes[i+1][j]!=0):
                    tmp+=1
                if(j<dim-1 and nb_of_shapes[i][j+1]!=0):
                    tmp+=1
                if(tmp<=1):
                    ans[nb_of_shapes[i][j]]+=1
    return max(ans)
    # Replace pass above with your code


# Possibly define other functions here
def dfs(x,y,c):
    res[x][y]=c
    if(x>0 and grid[x-1][y]==1):
        dfs(x-1,y,c)
    if(y>0 and grid[x][y-1]==1):
        dfs(x,y-1,c)
    if(x<dim-1 and grid[x+1][y]==1):
        dfs(x+1,y,c)
    if(y<dim-1 and grid[x][y+1]==1):
        dfs(x,y+1,c)
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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )