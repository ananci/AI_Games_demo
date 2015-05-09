import argparse
import random
import time

from maze_utilities import MazeUtilities

def random_search(x, y, maze):
    available_moves = MazeUtilities.get_available_moves(x, y, maze)
    #chose a random move
    choice_x, choice_y = random.choice(available_moves)
    return choice_x, choice_y

def return_unvisited(moves, maze):
    print moves
    choice_x, choice_y = random.choice(moves)
    moves.remove((choice_x, choice_y))

    if len(moves) == 0:
        return choice_x, choice_y
    if maze[choice_x][choice_y] != 3:
        return choice_x, choice_y
    else:
        return return_unvisited(moves, maze)

def no_backtrack_search(x, y, maze):
    available_moves = MazeUtilities.get_available_moves(x, y, maze)
    #chose a random move
    return return_unvisited(available_moves, maze)

def bfs_unvisited(moves, maze):
    print moves
    choice_x, choice_y = moves.pop(0)
    if len(moves) == 0:
        return choice_x, choice_y
    if maze[choice_x][choice_y] != 3:
        return choice_x, choice_y
    else:
        return return_unvisited(moves, maze)

def bfs_search(x, y, maze):
    available_moves = MazeUtilities.get_available_moves(x, y, maze)
    return bfs_unvisited(available_moves, maze)

def dfs_unvisited(moves, maze):
    print moves
    choice_x, choice_y = moves.pop()
    if len(moves) == 0:
        return choice_x, choice_y
    if maze[choice_x][choice_y] != 3:
        return choice_x, choice_y
    else:
        return return_unvisited(moves, maze)

def dfs_search(x, y, maze):
    available_moves = MazeUtilities.get_available_moves(x, y, maze)
    return dfs_unvisited(available_moves, maze)

def move(maze, x, y, search_func=random_search, path=[], delay=0):
    #print type(path)
    #print path
    if maze[x][y] == 2:
        print 'found at %d,%d' % (x, y)
        return None, None, path, True

    maze[x][y]='P'
    MazeUtilities.print_maze(maze=maze)
    #print 'visiting %d,%d' % (x, y)

    print search_func
    # search for your next move
    next_x, next_y = search_func(x, y, maze)
    if x == next_x and y == next_y:
        print "No Valid Moves"
        return None, None, path, False

    # mark as visited
    maze[x][y] = 3

    time.sleep(.25)
    path.append((x,y))
    return next_x, next_y, path, False

def path_finder(maze, x, y, search_func=random_search, delay=0, potential_pos, ):
    completed = False
    out_of_moves = False
    path = [(x, y)]
    new_x = x
    new_y = y
    while (not completed) and x is not None and y is not None:
        new_x, new_y, path, completed = move(maze, new_x, new_y, search_func=search_func, path=path, delay=delay)
    return path, completed

if __name__ == "__main__":

    # create the maze
    maze = MazeUtilities.generate_random_maze(10,10)

    # get the starting position
    x, y = MazeUtilities.get_starting_point(maze=maze, random=False)

    start = time.time()
    path, success = path_finder(maze, x, y, dfs_search, delay=0.25)
    time_delta = time.time() - start

    if success:
        print "You found the exit!"
        print "It took {N} moves.".format(len(path))
        print "It took {N} seconds.".format(time_delta)
