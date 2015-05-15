# AI Games and Demos
## for PyLadies San Antonio

This repository contains python modules chosen to demonstrate fundamental concepts and historical perspectives of AI. Copyright information is available in each module or, if appropriate, in folders containing modules. Modules and methods have been selected from around the internet and credit has been given when possible.

This repository is a work in progress. Use at your own risk.

- - -

## In This Repository

### /maze
/maze contains maze.py. This python script demonstrates basic pathfinding and maze solving using DFS, BFS, a random search and with hooks to allow a user to implement their own search algorithm.

**TO RUN**
1. Go into the /maze directory
2. Run the maze.py file

EXAMPLE
```
$ python maze.py

GENERATED MAZE:
STARING AT (1, 1)
GOAL AT (29, 29)
+==============================================================+
|##############################################################|
|##::            ##      ##          ##      ##              ##|
|##  ######  ##  ##  ##  ##  ######  ##  ##  ##  ######  ##  ##|
|##      ##  ##  ##  ##      ##  ##      ##  ##      ##  ##  ##|
|######  ##  ######  ##########  ##########  ######  ##  ##  ##|
|##  ##  ##      ##          ##          ##          ##  ##  ##|
|##  ##  ######  ##########  ##  ######  ##############  ######|
|##      ##          ##  ##  ##      ##              ##      ##|
|##  ######  ######  ##  ##  ##########  ##  ##############  ##|
|##      ##      ##      ##  ##      ##  ##  ##              ##|
|######  ######  ##  ######  ##  ##  ######  ##  ##########  ##|
|##      ##  ##  ##  ##      ##  ##          ##      ##  ##  ##|
|##  ######  ##  ######  ######  ##  ##############  ##  ##  ##|
|##  ##      ##          ##      ##  ##              ##  ##  ##|
|##  ##  ##  ##################  ##  ##  ##############  ##  ##|
|##      ##  ##          ##      ##  ##          ##          ##|
|##########  ##  ######  ##  ##  ##############  ######  ######|
|##          ##  ##          ##  ##              ##  ##      ##|
|##  ##########  ##  ##############  ######  ######  ######  ##|
|##  ##          ##      ##      ##  ##  ##  ##      ##      ##|
|##  ######  ##############  ##  ##  ##  ##  ##  ######  ######|
|##  ##      ##              ##      ##  ##  ##      ##      ##|
|##  ##  ######  ######################  ##  ######  ######  ##|
|##  ##      ##                  ##              ##  ##      ##|
|##  ######  ##################  ##############  ##  ##########|
|##          ##              ##          ##      ##          ##|
|##########  ######  ######  ##########  ##################  ##|
|##      ##      ##      ##  ##          ##          ##      ##|
|##  ##########  ######  ##  ##  ##########  ##  ######  ######|
|##                      ##  ##              ##            EE##|
|##############################################################|
+==============================================================+


========================
MENU
========================
Please choose:
	 To view BFS path please enter 'BFS-PATH'
	 To view BFS results please enter 'BFS-RESULTS'
	 To view DFS path please enter 'DFS-PATH'
	 To view DFS results please enter 'DFS-RESULTS'
	 To exit please enter 'EXIT'
Please enter your selection:
```

**FOR HELP OR OPTIONS**
```
$ python maze.py -h
usage: maze.py [-h] [-x WIDTH] [-y HEIGHT] [-rs] [-rg] [-e] [-d DELAY]

Maze pathfinder demonstration

optional arguments:
  -h, --help            show this help message and exit
  -x WIDTH, --width WIDTH
                        Width of the maze.
  -y HEIGHT, --height HEIGHT
                        Height of the maze.
  -rs, --random_start   Set the start at a random position in the maze.
                        Defaults to upper left corner.
  -rg, --random_goal    Set the goal at a random position in the maze.
                        Defaults to lower right corner.
  -e, --empty           Use an empty maze(no walls) to demonstrate the search
                        function.
  -d DELAY, --delay DELAY
                        Timed delay for presenting the path of the solved
                        maze. Defaults to .25 seconds.
```

- - -

### /demos

/demos contains single file demonstrations of some AI related concepts.

#### eliza.py
FROM: http://www.jezuk.co.uk/cgi-bin/view/software/eliza

(ELIZA)[http://en.wikipedia.org/wiki/ELIZA] was a famous natural-language program from the 1960's. Here Jez Higgins has modified an earlier implementation of ELIZA into a python script.


**TO RUN**
1. Go into the /demos directory
2. Run the eliza.py file

EXAMPLE
```
$ python eliza.py
Therapist
---------
Talk to the program by typing in plain English, using normal upper-
and lower-case letters and punctuation.  Enter "quit" when done.
========================================================================
Hello.  How are you feeling today?
>Pretty Good and you?
Please consider whether you can answer your own question.
>
```
