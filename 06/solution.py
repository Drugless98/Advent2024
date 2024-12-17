import time
import numpy as np
import re

class Map:
    def __init__(self, data):
        self.Board: list[list[str]]             = []
        self.Obstructions: list[tuple[int,int]] = []
        self.X_count = 0

        for line in range(len(data)):
            self.Board.append(list(data[line].replace("\n","")))

            if "^" in data[line]:
                self.Pos = (line, data[line].find("^"), "^")        #: Save pos of guard
            elif "#" in data[line]:
                for obs in re.finditer("#", data[line]):
                    self.Obstructions.append([line, obs.span()[0]]) #: Save array of obstruction coordinates

        self.Board = np.array(self.Board)
        self.Obstructions = np.array(self.Obstructions)

    def turn(self, direction: str):
        match direction:
            case "^":
                return ">"
            case ">":
                return "v"
            case "v":
                return "<"
            case "<":
                return "^"

    def add_obstacle(self, pos: tuple[int, int]):
        self.Obstructions = np.vstack([self.Obstructions, pos[0:2]]) #: Append the pos to the end of obstructions
        self.Board[pos[0]][pos[1]] = "#"

    def iterate(self): #: Return True if done otherwise False
        match self.Pos:
            case (Y, X, "^"):
                obstructions = np.where(self.Board[:,X] == "#")[0]
                if Y == 0:
                    return True
                elif Y-1 not in obstructions:
                    self.X_count = self.X_count if self.Board[Y-1][X] == "X" else self.X_count + 1
                    self.Board[Y][X] =   "X"
                    self.Board[Y-1][X] = "^"
                    self.Pos = (Y-1, X, "^")
                else:
                    self.Board[Y][X] = self.turn("^")
                    self.Pos = (Y, X, self.turn("^"))

                return False

            case (Y, X, ">"):
                obstructions = np.where(self.Board[Y] == "#")[0]
                if X == len(self.Board[X])-1:
                    return True
                if X+1 not in obstructions:
                    self.X_count = self.X_count if self.Board[Y][X+1] == "X" else self.X_count + 1
                    self.Board[Y][X] =   "X"
                    self.Board[Y][X+1] = ">"
                    self.Pos = (Y, X+1, ">")
                else:
                    self.Board[Y][X] = self.turn(">")
                    self.Pos = (Y, X, self.turn(">"))
                return False

            case (Y, X, "v"):
                obstructions = np.where(self.Board[:,X] == "#")[0]
                if Y == len(self.Board[:,Y])-1:
                    return True
                elif Y+1 not in obstructions:
                    self.X_count = self.X_count if self.Board[Y+1][X] == "X" else self.X_count + 1
                    self.Board[Y][X] =   "X"
                    self.Board[Y+1][X] = "v"
                    self.Pos = (Y+1, X, "v")
                else:
                    self.Board[Y][X] = self.turn("v")
                    self.Pos = (Y, X, self.turn("v"))
                return False

            case (Y, X, "<"):
                obstructions = np.where(self.Board[Y] == "#")[0]
                if X == 0:
                    return True
                if X-1 not in obstructions:
                    self.X_count = self.X_count if self.Board[Y][X-1] == "X" else self.X_count + 1
                    self.Board[Y][X] =   "X"
                    self.Board[Y][X-1] = "<"
                    self.Pos = (Y, X-1, "<")

                else:
                    self.Board[Y][X] = self.turn("<")
                    self.Pos = (Y, X, self.turn("<"))
                return False

def part_one():
    data_file = open("06\\input.txt").readlines()
    map = Map(data_file)
    while not map.iterate():
        continue
    return map.X_count+1

def part_two():
    data_file = open("06\\input.txt").readlines()
    map_simulate_and_find_loops  = Map(data_file)
    map_main_traverse            = Map(data_file)
    already_added_obstructions  = set()
    loop_counter                 = 0
    last_obstruction_pos         = [None, None, None]

    while not map_main_traverse.iterate():
        #reset simulation variables
        map_simulate_and_find_loops  = Map(data_file)
        visited = set()

        #Check if main turned this turn and skip this sim, otherwise this spot would count twice.
        if last_obstruction_pos[0:2] == map_main_traverse.Pos[0:2]:
            continue

        #Set obstacle on next position and check for loops
        map_simulate_and_find_loops.add_obstacle(map_main_traverse.Pos)
        last_obstruction_pos = map_main_traverse.Pos
        while not map_simulate_and_find_loops.iterate():
            #Check if obstruction already added, skip if it is
            if map_main_traverse.Pos[0:2] in already_added_obstructions:
                break

            if map_simulate_and_find_loops.Pos in visited:
                already_added_obstructions.add(map_main_traverse.Pos[0:2]) #: add obstruction to skip any other attempts to test same position
                loop_counter = loop_counter + 1
                break
            visited.add(map_simulate_and_find_loops.Pos)
    return loop_counter







if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")