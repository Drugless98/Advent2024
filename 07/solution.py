import time
import numpy as np

class rope_bridge:
    def __init__(self, goal, values_arr):
        self.Goal = goal
        self.stack= []
        self.stack.append(values_arr)

    def calibrate(self):
        
            
        

def part_one():
    data_file = open("07\\input.txt", "r").read()
    data      = data_file.split("\n")

    #: Parse data into Tree class
    calibrations = [rope_bridge(int(i.split(":")[0]), [int(n) for n in i.split(" ")[1:]]) for i in data]

    
def part_two():
    pass


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")