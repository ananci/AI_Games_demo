#----------------------------------------------------------------------
#  maze.py
#  requires maze_utilities.py
#
#  A simple maze demonstration script. Automatically generates a
#  solvable maze and then solves it using DFS and BFS search algorithms.
#
#  AUTHOR - Anna Eilering
#  LAST REVISED - 5/15/15
#----------------------------------------------------------------------
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

def print_results(results):
    print "="*24
    print "RESULTS"
    print "="*24
    for search_method, result in results.iteritems():
        print search_method
        print result
        print "-"*24

def print_menu(methods, results, maze, delay):

    while True:
        temp_maze = copy.deepcopy(maze)
        print "="*24
        print "MENU"
        print "="*24
        print "Please choose:"
        for item in results:
            print "\t To view {item} path please enter '{item}-PATH'".format(item=item)
            print "\t To view {item} results please enter '{item}-RESULTS'".format(item=item)
        print "\t To exit please enter 'EXIT'"

        in_value = raw_input("Please enter your selection: ")
        in_value = in_value.upper()

        if in_value == "EXIT":
            break
        elif "-PATH" in in_value:
            in_path = in_value.replace("-PATH", "")
            path = methods[in_path]
            for move in path:
                x, y = move
                temp_maze = MazeUtilities.move(maze=temp_maze, x=x, y=y)
                MazeUtilities. print_maze_small(temp_maze)
                time.sleep(delay)
        elif "-RESULTS" in in_value:
            in_res = in_value.replace("-RESULTS", "")
            print in_res
            res = results[in_res]
            print res
        else:
            print "Not a valid input"
        print ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maze pathfinder demonstration')

    parser.add_argument("-x", "--width", default=15, type=int,
                        help="Width of the maze.")
    parser.add_argument("-y", "--height", default=15, type=int,
                        help="Height of the maze.")
    parser.add_argument("-rs", "--random_start", action="store_true",
                        help=("Set the start at a random position in the maze."
                               " Defaults to upper left corner."))
    parser.add_argument("-rg", "--random_goal", action="store_true",
                        help=("Set the goal at a random position in the maze."
                              " Defaults to lower right corner."))
    parser.add_argument("-e", "--empty", action="store_true",
                        help=("Use an empty maze(no walls) to demonstrate the "
                              "search function."))
    parser.add_argument("-d", "--delay", default=.25, type=float,
                        help=("Timed delay for presenting the path of the "
                              "solved maze. Defaults to .25 seconds."))

    args = parser.parse_args()

    width = args.width
    height = args.height
    random_start = args.random_start
    random_goal = args.random_goal
    empty = args.empty
    delay = args.delay

    print "\nGENERATED MAZE:"
    if empty:
        maze=MazeUtilities.generate_empty_maze(w=width, h=height)
    else:
        maze = MazeUtilities.generate_random_maze(w=width, h=height)

    start_node = MazeUtilities.get_starting_point(maze=maze, random=random_start)
    print "STARING AT {0}".format(start_node)
    end_node = MazeUtilities.get_ending_point(maze=maze, random=random_goal)
    print "GOAL AT {0}".format(end_node)

    goal_x, goal_y = end_node
    start_x, start_y = start_node
    maze[goal_y][goal_x] = 2
    maze[start_y][start_x] = 'P'
    MazeUtilities.print_maze_small(maze=maze)
    #maze[start_y][start_x] = '0'

    methods = {}

    start = time.time()
    dfs_path = depthFirst(start_node, maze)
    dfs_time_delta = time.time() - start
    dfs_maze = copy.deepcopy(maze)
    methods["DFS"] = dfs_path

    results = {}

    if dfs_path:
        dfs_results = []
        dfs_results.append("DFS found the exit!")
        dfs_results.append("It took {N} moves.".format(N=len(dfs_path)))
        dfs_results.append("It took {N} seconds.".format(N=dfs_time_delta))
        results["DFS"] = "\n".join(dfs_results)
    else:
        results["DFS"] = "DFS was unable to find the path."

    start = time.time()
    bfs_path = breadthFirst(start_node, maze)
    bfs_time_delta = time.time() - start
    bfs_maze = copy.deepcopy(maze)
    methods["BFS"] = bfs_path

    if dfs_path:
        bfs_results = []
        bfs_results.append("BFS found the exit!")
        bfs_results.append("It took {N} moves.".format(N=len(bfs_path)))
        bfs_results.append("It took {N} seconds.".format(N=bfs_time_delta))
        results["BFS"] = "\n".join(bfs_results)
    else:
        results["BFS"] = "BFS was unable to find the path."

    print_menu(methods, results, maze, delay)
