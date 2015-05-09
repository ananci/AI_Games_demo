import random
import time

class MazeUtilities(object):
    """
    Class containing general maze utilities.

    All methods in this class should be static.
    """

    @staticmethod
    def generate_random_maze(x=10, y=10, wall_chance=20):
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

    @staticmethod
    def get_starting_point(maze, random=False):
        if random:
            x = random.randomInt(0, x-1)
            y = random.randomInt(0, y-1)
            while not MazeUtilities.is_valid(x, y, maze):
                x = random.randomInt(0, x-1)
                y = random.randomInt(0, y-1)
        else:
            # start in the upper left hand corner
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

    @staticmethod
    def is_valid(x, y, maze):
        x_is_valid = (-1 < x < len(maze) - 1 and maze[x][y] != 1)
        if x_is_valid:
            y_is_valid = (-1 < y < len(maze[x]) - 1 and maze[x][y] != 1)
        else:
            return False
        return (x_is_valid and y_is_valid)

    @staticmethod
    def get_available_moves(x, y, maze):
        # moves is a list of tuples (x,y)
        moves = []

        # try to the left of x
        if MazeUtilities.is_valid(x-1, y, maze):
            moves.append((x-1, y))
        # try to the right of x
        if MazeUtilities.is_valid(x+1, y, maze):
            moves.append((x+1, y))
        # try above y
        if MazeUtilities.is_valid(x, y-1, maze):
            moves.append((x, y-1))
        # try below y
        if MazeUtilities.is_valid(x, y+1, maze):
            moves.append((x, y+1))
        return moves
