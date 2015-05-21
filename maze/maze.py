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

def my_search(startingNode, maze):
    """
    Change this method to implement the search method of your choice.
    """
    visitedNodes = []
    ls = [startingNode]
    #print stack

    while len(ls) > 0:
        #node = ls.pop()
        node = random.choice(ls)
        ls.remove(node)
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
                ls.append(n)
    return visitedNodes

def random_search(startingNode, maze):
    """
    Random Search Implementation.

    Random implementation that keeps track of visited nodes. Uses a list as a
    queue. Returns the list of visited nodes.
    """
    visitedNodes = []
    ls = [startingNode]
    #print stack

    while len(ls) > 0:
        #node = ls.pop()
        node = random.choice(ls)
        ls.remove(node)
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
                ls.append(n)
    return visitedNodes

def depth_first(startingNode, maze):
    """
    Depth First Search Implementation.

    DFS implementation that keeps track of visited nodes. Uses a list as a
    stack. Returns the list of visited nodes.
    """
    visitedNodes = []
    ls = [startingNode]
    #print stack

    while len(ls) > 0:
        #node = ls.pop()
        node = ls[-1]
        ls.remove(node)
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
                ls.append(n)
    return visitedNodes

def breadth_first(startingNode, maze):
    """
    Breadth First Search Implementation.

    BFS implementation that keeps track of visited nodes. Uses a list as a
    queue. Returns the list of visited nodes.
    """
    visitedNodes = []
    ls = [startingNode]
    #print stack

    while len(ls) > 0:
        #node = ls.pop()
        node = ls[0]
        ls.remove(node)
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
                ls.append(n)
    return visitedNodes

def print_results(results):
    print("="*24)
    print("RESULTS")
    print("="*24)
    for search_method, result in results.iteritems():
        print(search_method)
        print(result)
        print("-"*24)

def print_menu(methods, results, maze, delay):

    while True:
        temp_maze = copy.deepcopy(maze)
        print("="*24)
        print("MENU")
        print("="*24)
        print("Please choose:")
        for item in results:
            print("\t To view {item} path please enter '{item}-PATH'".format(item=item))
            print("\t To view {item} results please enter '{item}-RESULTS'".format(item=item))
        print("\t To view all results please enter 'ALL'")
        print("\t To regenerate the maze and paths please enter 'AGAIN'")
        print("\t To exit please enter 'EXIT'")

        in_value = raw_input("Please enter your selection: ")
        in_value = in_value.upper()

        if in_value == "EXIT":
            return False
        if in_value == "AGAIN":
            return True

        if in_value == "ALL":
            for key, value in results.iteritems():
                print("-"*24)
                print(value)

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
            print(in_res)
            res = results[in_res]
            print(res)
        else:
            print("Not a valid input")
        print("")
    # Just in case
    return False

def main(width, height, random_start, random_goal, empty, delay, starting_node=None, ending_node=None, maze=None):
        print("\nGENERATED MAZE:")
        if maze:
            pass
        elif empty:
            maze=MazeUtilities.generate_empty_maze(w=width, h=height)
        else:
            maze = MazeUtilities.generate_random_maze(w=width, h=height)

        if starting_node:
            start_node = starting_node
        else:
            start_node = MazeUtilities.get_starting_point(maze=maze, random=random_start)
        print("STARING AT {0}".format(start_node))

        if ending_node:
            end_node = ending_node
        else:
            end_node = MazeUtilities.get_ending_point(maze=maze, random=random_goal)
        print("GOAL AT {0}".format(end_node))

        goal_x, goal_y = end_node
        start_x, start_y = start_node
        maze[goal_y][goal_x] = 2
        maze[start_y][start_x] = 'P'
        MazeUtilities.print_maze_small(maze=maze)
        #maze[start_y][start_x] = '0'

        methods = {}

        start = time.time()
        dfs_path = depth_first(start_node, maze)
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
        bfs_path = breadth_first(start_node, maze)
        bfs_time_delta = time.time() - start
        bfs_maze = copy.deepcopy(maze)
        methods["BFS"] = bfs_path

        if bfs_path:
            bfs_results = []
            bfs_results.append("BFS found the exit!")
            bfs_results.append("It took {N} moves.".format(N=len(bfs_path)))
            bfs_results.append("It took {N} seconds.".format(N=bfs_time_delta))
            results["BFS"] = "\n".join(bfs_results)
        else:
            results["BFS"] = "BFS was unable to find the path."

        start = time.time()
        random_path = random_search(start_node, maze)
        random_time_delta = time.time() - start
        random_maze = copy.deepcopy(maze)
        methods["RANDOM"] = random_path

        if random_path:
            random_results = []
            random_results.append("RANDOM SEARCH found the exit!")
            random_results.append("It took {N} moves.".format(N=len(random_path)))
            random_results.append("It took {N} seconds.".format(N=random_time_delta))
            results["RANDOM"] = "\n".join(random_results)
        else:
            results["RRANDOM"] = "RANDOM SEARCH was unable to find the path."

        # This is your custom search
        start = time.time()
        my_path = random_search(start_node, maze)
        my_time_delta = time.time() - start
        my_maze = copy.deepcopy(maze)
        methods["CUSTOM"] = my_path

        if my_path:
            my_results = []
            my_results.append("CUSTOM SEARCH found the exit!")
            my_results.append("It took {N} moves.".format(N=len(my_path)))
            my_results.append("It took {N} seconds.".format(N=my_time_delta))
            results["CUSTOM"] = "\n".join(my_results)
        else:
            results["CUSTOM"] = "CUSTOM SEARCH was unable to find the path."

        return print_menu(methods, results, maze, delay)


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
    parser.add_argument("-f", "--file", default=None,
                        help=("A filepath containing a previously "
                              "generated maze"))

    args = parser.parse_args()

    width = args.width
    height = args.height
    random_start = args.random_start
    random_goal = args.random_goal
    empty = args.empty
    delay = args.delay
    filepath = args.file

    starting_node = None
    ending_node = None
    maze = None

    if filepath:
        with open(filepath, 'r') as f:
            raw_maze = f.readlines()
        starting_node, ending_node, maze = MazeUtilities.convert_to_maze(raw = raw_maze)

    while True:
        ret_val = main(width, height, random_start, random_goal, empty, delay, starting_node, ending_node, maze)
        if not ret_val:
            break
