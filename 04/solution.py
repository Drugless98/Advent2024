import time
import numpy as np
import numpy.typing as npt
import re


class Table:
    def __init__(self, data_table):
        self.Line_to_check = []
        self.Data_Table = []
        for row in data_table:
            arr_row = []
            for letter in row:
                arr_row.append(letter)
            self.Data_Table.append(arr_row)
    
    def add_horizontal_rows(self):
        for row in self.Data_Table:
            self.Line_to_check.append(row)
            self.Line_to_check.append(row[::-1])
    
    def add_vertical_rows(self):
        for col in range(len(self.Data_Table[0])):
            self.Line_to_check.append(np.array(self.Data_Table)[:,col].tolist())
            self.Line_to_check.append(np.array(self.Data_Table)[:,col][::-1].tolist())
    
    def add_diagonal_rows_SE_and_NW(self):
        diagonal_index = 1
        col_counter = 1
        for row in range(len(self.Data_Table) + len(self.Data_Table[0])-1):
            row_arr = []
            if row < len(self.Data_Table):
                for index in range(diagonal_index):
                    row_arr.append(self.Data_Table[row-index][-1-index])
                diagonal_index += 1
            else:
                diagonal_index -= 1
                for index in range(1, diagonal_index):
                    y = len(self.Data_Table)-index-col_counter
                    x = len(self.Data_Table[0])-index
                    row_arr.append(self.Data_Table[x][y])
                col_counter += 1
            self.Line_to_check.append(row_arr)
            self.Line_to_check.append(row_arr[::-1])
    
    def add_diagonal_rows_NE_and_SW(self):
        diagonal_index = 1
        col_counter = 1
        for row in range(len(self.Data_Table) + len(self.Data_Table[0])-1):
            row_arr = []
            if row < len(self.Data_Table):
                for index in range(diagonal_index):
                    row_arr.append(self.Data_Table[row-index][index])
                diagonal_index += 1
            else:
                diagonal_index -= 1
                for index in range(diagonal_index-1):
                    y = index+col_counter
                    x = len(self.Data_Table[0])-index-1
                    row_arr.append(self.Data_Table[x][y])
                col_counter += 1
            self.Line_to_check.append(row_arr)
            self.Line_to_check.append(row_arr[::-1])
    
    def count_occurrence(self, string_to_find: str):
        sum = 0
        for line in self.Line_to_check:
            line = ("").join(line)
            sum += len(re.findall(f"({string_to_find})", line))
        return sum


def part_one():
    data_file = open("04\\input.txt", "r").readlines()
    data      = [dataline.replace("\n", "").replace(".", "K") for dataline in data_file]

    table = Table(data)
    table.add_horizontal_rows()
    table.add_vertical_rows()
    table.add_diagonal_rows_SE_and_NW()
    table.add_diagonal_rows_NE_and_SW()
    return table.count_occurrence("XMAS")


def part_two():
    data_file = open("04\\input.txt", "r").readlines()
    data      = [dataline.replace("\n", "").replace(".", "K") for dataline in data_file]

    table = Table(data)
    sum = 0

    for y in range(len(table.Data_Table)):
        for x in range(len(table.Data_Table[0])):
            max_Y = len(table.Data_Table)-1
            max_X = len(table.Data_Table[0])-1
            if x == 0 or y == 0 or x == max_X or y == max_Y:
                continue
            elif table.Data_Table[y][x] == "A":    
                    NW_letter = table.Data_Table[y-1][x-1]
                    NE_letter = table.Data_Table[y-1][x+1]
                    SW_letter = table.Data_Table[y+1][x-1]
                    SE_letter = table.Data_Table[y+1][x+1]

                    pair_one = NW_letter + SE_letter
                    pair_two = NE_letter + SW_letter

                    xmas: bool = (pair_one == "MS" or pair_one == "SM") and (pair_two == "MS" or pair_two == "SM")
                    sum = sum + 1 if xmas else sum
            else:
                continue
    return sum

if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")