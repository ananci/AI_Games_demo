import argparse
import copy
import random
import time

from maze_utilities import MazeUtilities

def random_search(x, y, maze):
    available_moves = MazeUtilities.get_available_moves(x=x, y=y, maze=maze)
    #chose a random move
    choice_x, choice_y = random.choice(available_moves)
    return choice_x, choice_y

def depthFirst(startingNode, maze):
    visitedNodes = []
    stack = [startingNode]
    #print stack

    while len(stack) > 0:
        node = stack.pop()
        #print "NODE:" +  str(node)
        if node in visitedNodes:
            continue

        visitedNodes.append(node)
        x, y = node
        if maze[y][x] == 2:
            return visitedNodes

        children = MazeUtilities.get_available_moves(x=x, y=y, maze=maze)
        #print children
        for n in children:
            if n not in visitedNodes:
                stack.append(n)
    return visitedNodes

def breadthFirst(startingNode, maze):
    visitedNodes = []
    stack = [startingNode]
    #print stack

    while len(stack) > 0:
        node = stack.pop(0)
        #print "NODE:" +  str(node)
        if node in visitedNodes:
            continue

        visitedNodes.append(node)
        x, y = node
        if maze[y][x] == 2:
            return visitedNodes

        children = MazeUtilities.get_available_moves(x=x, y=y, maze=maze)
        #print children
        for n in children:
            if n not in visitedNodes:
                stack.append(n)
    return visitedNodes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maze pathfinder demonstration')

    parser.add_argument("-x", "--width", default=15, type=int, help="Width of the maze.")
    parser.add_argument("-y", "--height", default=15, type=int, help="Height of the maze.")
    parser.add_argument("-rs", "--random_start", action='store_true', help="Set the start at a random position in the maze. Defaults to upper left corner.")
    parser.add_argument("-rg", "--random_goal", action='store_true', help="Set the goal at a random position in the maze. Defaults to lower right corner.")

    args = parser.parse_args()

    width = args.width
    height = args.height
    random_start = args.random_start
    random_goal = args.random_goal

    print "\nGENERATED MAZE:"
    maze = MazeUtilities.generate_random_maze(w=width, h=height)

    start_node = MazeUtilities.get_starting_point(maze=maze, random=random_start)
    print "STARING AT {0}".format(start_node)
    end_node = MazeUtilities.get_ending_point(maze=maze, random=random_goal)
    print "GOAL AT {0}".format(end_node)

    goal_x, goal_y = end_node
    maze[goal_y][goal_x] = 2
    MazeUtilities.print_maze_small(maze=maze)

    methods = {}

    start = time.time()
    dfs_path = depthFirst(start_node, maze)
    dfs_time_delta = time.time() - start
    dfs_maze = copy.deepcopy(maze)
    methods["dfs"] = dfs_path

    start = time.time()
    bfs_path = breadthFirst(start_node, maze)
    bfs_time_delta = time.time() - start
    bfs_maze = copy.deepcopy(maze)
    methods["dfs"] = bfs_path
    #print maze
    #MazeUtilities.print_maze_small(dfs_maze)
    for each_move in dfs_path:
        x, y = each_move
        dfs_maze = MazeUtilities.move(dfs_maze, x=x, y=y)
        MazeUtilities.print_maze_small(dfs_maze)

    if dfs_path:
        print "DFS"
        print "You found the exit!"
        print "It took {N} moves.".format(N=len(dfs_path))
        print "It took {N} seconds.".format(N=dfs_time_delta)

    """for each_move in bfs_path:
        x, y = each_move
        bfs_maze = MazeUtilities.move(bfs_maze, x=x, y=y)
        MazeUtilities.print_maze_small(bfs_maze)"""

    if bfs_path:
        print "BFS"
        print "You found the exit!"
        print "It took {N} moves.".format(N=len(bfs_path))
        print "It took {N} seconds.".format(N=bfs_time_delta)
