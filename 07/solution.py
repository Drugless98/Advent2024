import time
import numpy as np

class Tree:
    class Node:
        def __init__(self, val, left= None, right= None):
            self.Val   = val
            self.Left  = left  # subtract 
            self.Right = right # Devide

    def __init__(self, root, values_arr):
        self.Root    = self.Node(root)
        self.Values  = values_arr
        self.counter = len(self.Values)
        self.operators: list[str] = []
    
    def make(self, hight, node: Node, parent: Node):
        if node.Val == 1 and node == parent.Right:
            return True
        elif node.Val == 0 and node == parent.Left:
            return True
               
        node.Left  = self.Node(node.Val - self.Values[len(self.Values) - hight - 1])
        node.Right = self.Node(node.Val / self.Values[len(self.Values) - hight - 1])

        if hight > len(self.Values):
            return None
        elif self.make(hight+1, node.Left, node):
            self.operators.append("+")
            return True
        elif self.make(hight+1, node.Right, node):
            self.operators.append("*")
            return True
        else:
            return None
            
        

def part_one():
    data_file = open("07\\input.txt", "r").read()
    data      = data_file.split("\n")

    #: Parse data into Tree class
    calibrations = [Tree(int(i.split(":")[0]), [int(n) for n in i.split(" ")[1:]]) for i in data]

    #: Make Tree
    for calibration in calibrations:
        calibration.make(0, calibration.Root, calibration.Root)
    
    #: Find sum
    sum = 0
    for calibration in calibrations:
        if len(calibration.operators) > 0:
            sum = sum + calibration.Root.Val
    return sum
    
def part_two():
    pass


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")