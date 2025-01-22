import time
import os
import numpy as np


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return an item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(index=0)
    
    def contains(self, item):
        """Check if an item is in the queue"""
        return item in self.queue
            
class Calibration:
    def parse_data(self, input_str: str):
        parse_data = input_str.split(": ")
        goal    = parse_data[0]
        numbers = parse_data[1].split(" ")
        return (goal, numbers)

    def __init__(self, calbration_with_no_operators: str):
        parsed_data = self.parse_data(calbration_with_no_operators)
        self.Goal   = int(parsed_data[0])
        self.Numbers= parsed_data[1]

def part_one():
    file_path = os.path.dirname(__file__)
    data_file = open(f"{file_path}\\input.txt", "r").read()
    data      = data_file.split("\n")

    calibrations = [Calibration(i) for i in data]
    sum = 0

    for calibration in calibrations:
        queue = Queue()
        queue.enqueue(int(calibration.Numbers[0]))

        for current in calibration.Numbers[1:]:
            numbers_on_queue = queue.queue
            queue.queue = []
        
            for i in numbers_on_queue:
                if i*int(current) <= calibration.Goal:
                    queue.enqueue(i * int(current))
                if i+int(current) <= calibration.Goal:
                    queue.enqueue(i + int(current))

        if queue.contains(calibration.Goal):
            sum += calibration.Goal    
    return sum
    
def part_two():
    file_path = os.path.dirname(__file__)
    data_file = open(f"{file_path}\\input.txt", "r").read()
    data      = data_file.split("\n")

    calibrations = [Calibration(i) for i in data]
    sum = 0

    for calibration in calibrations:
        queue = Queue()
        queue.enqueue(int(calibration.Numbers[0]))

        for current in calibration.Numbers[1:]:
            numbers_on_queue = queue.queue
            queue.queue = []
        
            for i in numbers_on_queue:
                if i*int(current) <= calibration.Goal:
                    queue.enqueue(i * int(current))
                if i+int(current) <= calibration.Goal:
                    queue.enqueue(i + int(current))
                if int(str(i) + str(current)) <= calibration.Goal:
                    queue.enqueue(int(str(i) + str(current))) 

        if queue.contains(calibration.Goal):
            sum += calibration.Goal    
    return sum


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")