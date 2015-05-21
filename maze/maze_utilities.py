#----------------------------------------------------------------------
#  maze_utilities.py
#
#  Utilities for a simple maze demonstration script.
#
#  AUTHOR - Anna Eilering
#  LAST REVISED - 5/15/15
#----------------------------------------------------------------------

import copy
import random
from random import shuffle, randrange
import time

class MazeUtilities(object):
    """
    Class containing general maze utilities.

    All methods in this class should be static.
    """

    @staticmethod
    def generate_empty_maze(w=20, h=20):
        maze = []
        top_row = [1]*(w*2 + 1)
        maze.append(top_row)
        for y in range(h):
            row = [1]
            for x in range(w):
                row.append(0)
                row.append(0)
            row.pop()
            row.append(1)
            maze.append(row)
            maze.append(row)
        maze.pop()
        maze.append(top_row)
        return maze

    @staticmethod
    def generate_random_maze(w=20, h=20):
        """
        Generate a random solveable maze with height and width w.

        :param h: (INT) the height of the maze, default 20
        :param w: (INT) the width of the maze, default 20
        :return maze: (LIST of LISTS) A list of length h containing containing
                      lists of length w representing a maze. Walls are defined
                      as 1, passages defined as 0.
        :raises ValueError: raises an exception if param values are too small
                            (less than 5), or too large (greater than 40).
        """

        if not (5 <= w <= 40):
            raise ValueError("width: {0} was not in the appropriate range of"
                             " 5 - 40".format(w))
        if not(5 <= h <= 40):
            raise ValueError("height: {0} was not in the appropriate range of"
                             " 5 - 40".format(h))
    	vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    	ver = [["10"] * w + ['1'] for _ in range(h)] + [[]]
    	hor = [["11"] * w + ['1'] for _ in range(h + 1)]

    	def walk(x, y):
    		vis[y][x] = 1

    		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    		shuffle(d)
    		for (xx, yy) in d:
    			if vis[yy][xx]: continue
    			if xx == x: hor[max(y, yy)][x] = "10"
    			if yy == y: ver[y][max(x, xx)] = "00"
    			walk(xx, yy)

    	walk(randrange(w), randrange(h))
    	maze = []
    	for (a, b) in zip(hor, ver):
    		if a:
    			row1 = ''.join(a)
    		row2 = ''.join(b)
    		r1_ls = []
    		r2_ls = []
    		for thing in row1:
    			thing = int(thing)
    			r1_ls.append(thing)
    		for thing in row2:
    			thing = int(thing)
    			r2_ls.append(thing)
    		if r1_ls:
    			maze.append(r1_ls)
    		if r2_ls:
    			maze.append(r2_ls)

    	return maze


    @staticmethod
    def get_starting_point(maze, random=False):
        if random:
            return MazeUtilities.get_random_point(maze=maze)
        else:
            # start in the upper left corner
            x = 0
            y = 0
            while not MazeUtilities.is_valid(x, y, maze):
                if x > len(maze) - 1:
                    x = 0
                if y > len(maze) - 1:
                    y = 0
                x = x + 1
                y = y + 1
        return x, y

    @staticmethod
    def get_ending_point(maze, random=False):
        if random:
            return MazeUtilities.get_random_point(maze=maze)
        else:
            # start in the bottom right corner
            x = len(maze[0]) - 1
            y = len(maze) - 1
            while not MazeUtilities.is_valid(x, y, maze):
                if x < 0:
                    x = len(maze[0]) - 1
                if y < 0:
                    y = len(maze) - 1
                x = x - 1
                y = y - 1
        return x, y

    @staticmethod
    def get_random_point(maze):
        w = len(maze[0]) - 1
        h = len(maze) - 1
        x = random.randint(0, w)
        y = random.randint(0, h)
        while not MazeUtilities.is_valid(x=x, y=y, maze=maze):
            x = random.randint(0, w)
            y = random.randint(0, h)
        return x, y

    @staticmethod
    def move(maze, x, y):
        # mark where we are
        #print maze
        if maze[y][x] == 2:
            maze[y][x]='**'
        maze[y][x]='P'

        #MazeUtilities.print_maze(maze)
        #time.sleep(0.25)

        return maze

    @staticmethod
    def print_maze(maze):
        print("+" + "="*len(maze[0])*4 + "+")
        for column in maze:
            row = ["|"]
            for position in column:
                if position == '1':
                    row.append("####")
                if position == 2:
                    row.append("!EE!")
                if position == 3:
                    row.append("::::")
                if position == 0:
                    row.append("    ")
                if position == 'P':
                    row.append("XXXX")
            row.append("|")
            print("".join(row))
            print("".join(row))
        print("+" + "="*len(maze[0])*4 + "+")
        print("\n")

    @staticmethod
    def print_maze_small(maze):
        print("+" + "="*len(maze[0])*2 + "+")
        for column in maze:
            row = ["|"]
            for position in column:
                if position == 1:
                    row.append("##")
                if position == 2:
                    row.append("EE")
                if position == 3:
                    row.append("::")
                if position == 0:
                    row.append("  ")
                if position == 'P':
                    row.append("::")
            row.append("|")
            #print "".join(row)
            print("".join(row))
        print("+" + "="*len(maze[0])*2 + "+")
        print("\n")


    @staticmethod
    def is_valid(x, y, maze):
        x_is_valid = (-1 < x < len(maze[0]))
        y_is_valid = (-1 < y < len(maze))
        if (x_is_valid and y_is_valid):
            return (maze[y][x] != 1)
        else:
            return False

    @staticmethod
    def get_available_moves(x, y, maze):
        # moves is a list of tuples (x,y)
        moves = []

        # try to the left of x
        if MazeUtilities.is_valid(x=x-1, y=y, maze=maze) and maze[y][x-1] != 3:
            moves.append((x-1, y))
        # try to the right of x
        if MazeUtilities.is_valid(x=x+1, y=y, maze=maze) and maze[y][x+1] != 3:
            moves.append((x+1, y))
        # try above y
        if MazeUtilities.is_valid(x=x, y=y-1, maze=maze) and maze[y-1][x] != 3:
            moves.append((x, y-1))
        # try below y
        if MazeUtilities.is_valid(x=x, y=y+1, maze=maze) and maze[y+1][x] != 3:
            moves.append((x, y+1))
        return moves

    @staticmethod
    def convert_to_maze(raw):
        maze = []
        for row in  raw:
            if "+" in row:
                continue
            else:
                row_ls = []
                row = row.replace("|", "")
                for i in xrange(0, len(row), 2):
                    block = row[i:i+2]
                    if block == "##":
                        row_ls.append(1)
                    elif block == "EE":
                        row_ls.append(2)
                    elif block == "::":
                        row_ls.append(3)
                    else:
                        row_ls.append(0)
                maze.append(row_ls)

        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0
        # now find the starting and ending points
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 3:
                    start_x = x
                    start_y = y
                if maze[y][x] == 2:
                    end_x = x
                    end_y = y
        return ((start_x, start_y), (end_x, end_y), maze)
