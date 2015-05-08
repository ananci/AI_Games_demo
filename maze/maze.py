import random
import time

def generate_random_maze(x,y, wall_chance=20):
    maze = []
    for col in range(x):
        row = []
        for pos in range(y):
            # we
            dice = random.randint(1,wall_chance)
            if dice == 1:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    # chose a random place for the exit
    x_exit = random.randint(0, x-1)
    y_exit = random.randint(0, y-1)
    maze[x_exit][y_exit]=2
    return maze

def print_maze(maze):
    print "="*24
    for column in maze:
        row = []
        for position in column:
            if position == 1:
                row.append("####")
            if position == 2:
                row.append("!EE!")
            if position == 3:
                row.append("::::")
            if position == 0:
                row.append("    ")
            if position == 'P':
                row.append("XXXX")
        print "".join(row)
        print "".join(row)
    print "="*24
    print "\n"

def is_valid(x, y, grid):
    print "X, Y : " + str(x) + ", " + str(y)
    x_is_valid = (-1 < x < len(grid) - 1 and grid[x][y] != 1)
    print "x is valid " + str(x_is_valid)
    if x_is_valid:
        y_is_valid = (-1 < y < len(grid[x]) - 1 and grid[x][y] != 1)
        print "y is valid " + str(y_is_valid)
    else:
        return False
    return (x_is_valid and y_is_valid)



def get_available_moves(x, y, grid):
    # moves is a list of tuples (x,y)
    moves = []

    # try to the left of x
    if is_valid(x-1, y, grid):
        moves.append((x-1, y))
    # try to the right of x
    if is_valid(x+1, y, grid):
        moves.append((x+1, y))
    # try above y
    if is_valid(x, y-1, grid):
        moves.append((x, y-1))
    # try below y
    if is_valid(x, y+1, grid):
        moves.append((x, y+1))
    return moves

def random_search(x, y, grid):
    available_moves = get_available_moves(x, y, grid)
    #chose a random move
    choice_x, choice_y = random.choice(available_moves)
    return choice_x, choice_y

def return_unvisited(moves, grid):
    print moves
    choice_x, choice_y = random.choice(moves)
    moves.remove((choice_x, choice_y))

    if len(moves) == 0:
        return choice_x, choice_y
    if grid[choice_x][choice_y] != 3:
        return choice_x, choice_y
    else:
        return return_unvisited(moves, grid)

def no_backtrack_search(x, y, grid):
    available_moves = get_available_moves(x, y, grid)
    #chose a random move
    return return_unvisited(available_moves, grid)

def bfs_unvisited(moves, grid):
    print moves
    choice_x, choice_y = moves.pop(0)
    if len(moves) == 0:
        return choice_x, choice_y
    if grid[choice_x][choice_y] != 3:
        return choice_x, choice_y
    else:
        return return_unvisited(moves, grid)

def bfs_search(x, y, grid):
    available_moves = get_available_moves(x, y, grid)
    return bfs_unvisited(available_moves, grid)

def dfs_unvisited(moves, grid):
    print moves
    choice_x, choice_y = moves.pop()
    if len(moves) == 0:
        return choice_x, choice_y
    if grid[choice_x][choice_y] != 3:
        return choice_x, choice_y
    else:
        return return_unvisited(moves, grid)

def dfs_search(x, y, grid):
    available_moves = get_available_moves(x, y, grid)
    return dfs_unvisited(available_moves, grid)

def move(grid, x, y, search_func=random_search):
    if grid[x][y] == 2:
        print 'found at %d,%d' % (x, y)
        return True

    grid[x][y]='P'
    print_maze(maze=grid)
    #print 'visiting %d,%d' % (x, y)

    # search for your next move
    next_x, next_y = search_func(x, y, grid)
    if x == next_x and y == next_y:
        print "No Valid Moves"
        return False

    # mark as visited
    grid[x][y] = 3

    time.sleep(.25)
    move(grid, next_x, next_y, search_func)



if __name__ == "__main__":
    x = 0
    y = 0
    grid = generate_random_maze(10,10)

    while grid[x][y]==1:
        #try moving to an empty spot
        if x < (len(grid) - 1):
            x += 1
        else:
            x = 0
        if y <(len(grid[x]) -1):
            y += 1
        else:
            y = 0
    move(grid, x, y, dfs_search)
