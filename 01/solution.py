import time
import numpy as np

def part_one():
    data = np.loadtxt("01\\input.csv", delimiter=";", dtype=int)

    first_col = np.sort(data[:,0])
    second_col= np.sort(data[:,1])
    distances = [np.abs(first_col[i]-second_col[i]) for i in range(len(first_col))]

    return np.sum(distances) 

def part_two():
    data = np.loadtxt("01\\input.csv", delimiter=";", dtype=int)

    first_col = data[:,0]
    second_col= data[:,1]
    sim_score = [first_col[i] * len(np.where(second_col == first_col[i])[0]) for i in range(len(first_col))]
    
    return np.sum(sim_score)


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")