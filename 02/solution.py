import time
import numpy as np


def part_one():
    data_file = open("02\\input.csv", "r").readlines()

    safe_count = 0
    for report in data_file:
        level      = report.replace("\n", "").split(";")
        level_diff = np.diff(np.array(level, dtype=int))                       # Array of diff for number on the right

        all_accending_and_within_limit  = len(np.where(level_diff > 0)[0]) == len(level_diff) and len(np.where(level_diff >  3)[0]) == 0  # Where diff is bigger than 0 
        all_deccending_and_within_limit = len(np.where(level_diff < 0)[0]) == len(level_diff) and len(np.where(level_diff < -3)[0]) == 0 # Where diff is lower than 0 

        safe_count = safe_count + 1 if all_accending_and_within_limit or all_deccending_and_within_limit else safe_count
    return safe_count
        # [1, 2, 6, 4, 5]

def part_two():
    def helper(arr: list[int]):
        level_diff = np.diff(np.array(arr, dtype=int)) 
        all_accending_and_within_limit  = len(np.where(level_diff > 0)[0]) == len(level_diff) and len(np.where(level_diff >  3)[0]) == 0  # Where diff is bigger than 0 
        all_deccending_and_within_limit = len(np.where(level_diff < 0)[0]) == len(level_diff) and len(np.where(level_diff < -3)[0]) == 0 # Where diff is lower than 0 
        return all_accending_and_within_limit or all_deccending_and_within_limit

    #: Data and input :#
    data_file = open("02\\input.csv", "r").readlines()
    safe_count = 0

    #: run :#
    for report in data_file:
        level      = report.replace("\n", "").split(";")
        if helper(level):
             safe_count = safe_count + 1
        else:
            for i in range(1, len(level)+1): ##: Eew, ugly ass nested loop.
                split_arry = level[0:i-1]
                sub_arr = split_arry + level[i:len(level)]
                
                if helper(sub_arr):
                    safe_count = safe_count + 1
                    break
    return safe_count

if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")
    print()

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved part two in: {time.time()-start_time} Seconds")