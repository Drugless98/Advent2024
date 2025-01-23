import time
import os
import numpy as np

class Grid:
    class Point:
        def __init__(self, x, y, symbol):
            self.X = x
            self.Y = y
            self.Symbol = symbol

    def __init__(self, lines):
        self.__Raw_Grid = np.array([list(line) for line in lines])
        self.__Points: list[self.Point] = []
        self.Size = (len(self.__Raw_Grid), len(self.__Raw_Grid[0]))
        self.Symbol_dict = {}

        for i in range(len(self.__Raw_Grid)):
            row = []
            for j in range(len(self.__Raw_Grid[i])):
                new_point = self.Point(i,j, self.__Raw_Grid[i][j])
                row.append(new_point)

                if new_point.Symbol == ".":
                    continue
                elif new_point.Symbol in self.Symbol_dict.keys():
                    self.Symbol_dict[new_point.Symbol] = {"x" : self.Symbol_dict[new_point.Symbol]["x"] + [new_point.X], "y" : self.Symbol_dict[new_point.Symbol]["y"] + [new_point.Y]}
                else:
                    self.Symbol_dict[new_point.Symbol] = {"x" : [new_point.X], "y" : [new_point.Y]}
            self.__Points.append(row)

    # Functions
    def dist_vector(self, p1: Point, p2: Point) -> tuple[int, int]:
        return (p2.X - p1.X, p2.Y - p1.Y)

    def move_point(self, p1: Point, vect: tuple[int, int], subtract=False) -> Point:
        return self.Point(p1.X - vect[0], p1.Y - vect[1], "#") if subtract else  self.Point(p1.X + vect[0], p1.Y + vect[1], "#")
    
    def point_validate(self, p: Point) -> bool:
        x_valid = p.X >= 0 and p.X < self.Size[0]
        y_valid = p.Y >= 0 and p.Y < self.Size[1]
        return x_valid and y_valid

    # Getters
    def get_row(self, row_nr) -> list[Point]: return [i for i in self.__Points[row_nr]]
    def get_col(self, col_nr) -> list[Point]: return [row[col_nr] for row in self.__Points]
    def get_point(self, x, y) -> Point      : return self.get_row(x)[y]
    def get_grid(self): return self.__Raw_Grid
    



def part_one():
    file_path = os.path.dirname(__file__)
    data_file = open(f"{file_path}\\input.txt", "r").read()
    data      = data_file.split("\n")

    grid = Grid(data)
    anti_nodes = set()

    for symbol in grid.Symbol_dict:
        Xs = grid.Symbol_dict[symbol]["x"]
        Ys = grid.Symbol_dict[symbol]["y"]

        for node_index in range(len(Xs)):
            p = grid.get_point(Xs[node_index], Ys[node_index])

            for iterate_dict in range(node_index+1, len(Xs)):
                target_point = grid.get_point(Xs[iterate_dict], Ys[iterate_dict])
                
                new_point_1 = grid.move_point(p           , grid.dist_vector(target_point, p))
                new_point_2 = grid.move_point(target_point, grid.dist_vector(p, target_point))
                
                if grid.point_validate(new_point_1):
                    anti_nodes.add((new_point_1.X, new_point_1.Y))
                if grid.point_validate(new_point_2):
                    anti_nodes.add((new_point_2.X, new_point_2.Y))
    return len(anti_nodes)

def part_two():
    file_path = os.path.dirname(__file__)
    data_file = open(f"{file_path}\\input.txt", "r").read()
    data      = data_file.split("\n")

    grid = Grid(data)
    anti_nodes = set()

    for symbol in grid.Symbol_dict:
        Xs = grid.Symbol_dict[symbol]["x"]
        Ys = grid.Symbol_dict[symbol]["y"]

        for node_index in range(len(Xs)):
            p = grid.get_point(Xs[node_index], Ys[node_index])
            anti_nodes.add((p.X, p.Y))

            for iterate_dict in range(node_index+1, len(Xs)):
                target_point = grid.get_point(Xs[iterate_dict], Ys[iterate_dict])
                anti_nodes.add((target_point.X, target_point.Y))
                
                new_point_1 = grid.move_point(p           , grid.dist_vector(target_point, p))
                new_point_2 = grid.move_point(target_point, grid.dist_vector(p, target_point))
                
                temp_p = p
                temp_target = target_point
                while grid.point_validate(new_point_1):
                    anti_nodes.add((new_point_1.X, new_point_1.Y))
                    anti_nodes.add((temp_target.X, temp_target.Y))
                    anti_nodes.add((temp_p.X, temp_p.Y))

                    temp_target = temp_p
                    temp_p = new_point_1
                    new_point_1 = grid.move_point(new_point_1, grid.dist_vector(temp_target, temp_p))

                temp_p = p
                temp_target = target_point
                while grid.point_validate(new_point_2):
                    anti_nodes.add((new_point_2.X, new_point_2.Y))
                    anti_nodes.add((temp_p.X, temp_p.Y))
                    anti_nodes.add((temp_target.X, temp_target.Y))

                    temp_p = temp_target
                    temp_target = new_point_2
                    new_point_2 = grid.move_point(new_point_2, grid.dist_vector(temp_p, temp_target))
                



    temp_grid = grid.get_grid()
    f = open("notes.txt", "w")
    for i in anti_nodes:
        temp_grid[i[0]][i[1]] = "#"
    for row in temp_grid:
        for j in row:
            f.write(f"{j}")
        f.write("\n")
    return len(anti_nodes)


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")