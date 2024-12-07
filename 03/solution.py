import time
import numpy as np
import re

def part_one():
    def mul_calc(t: tuple[str, str]):
        X, Y = t
        return int(X) * int(Y)

    ##: Data input
    data_file = open("03\\input.txt", "r")
    data      = data_file.read()

    ##: Variables
    sum = 0
    multiplications = re.findall("mul\(([0-9]*),([0-9]*)\)", data)

    ##: calcs
    for mul in multiplications:
        sum = sum + mul_calc(mul)
    return sum

def part_two():
    def mul_calc_v2(t: str):
        X, Y = re.findall("mul\(([0-9]*),([0-9]*)\)", t)[0]
        return int(X) * int(Y)

    ##: Data input
    data_file = open("03\\input.txt", "r")
    data      = data_file.read()

    ##: Variables
    sum = 0
    flag = True

    ##: Calc
    multiplications = re.findall("(don't\(\)|do\(\)|mul\([0-9]*,[0-9]*\))", data)
    for exp in multiplications:
        match exp:
            case "do()":
                flag = True
            case "don't()":
                flag = False
            case _:
                sum = sum + mul_calc_v2(exp) if flag else sum
    return sum

if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")