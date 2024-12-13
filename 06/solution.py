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
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # print(map.Board)
        # time.sleep(0.5)
        continue
    return map.X_count+1

def part_two():
    pass


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")