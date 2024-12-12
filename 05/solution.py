import time
import numpy as np    

class Graph:
    class Node:
        def __init__(self, val):
            self.Value = val
            self.Next = []

    def __init__(self):
        self.Nodes: dict[self.Node] = {}
        self.Node_values = []

    def add_rule(self, low_val, high_val):
        if high_val not in self.Node_values:
            self.Node_values.append(high_val)
            self.Nodes[high_val] = self.Node(high_val)

        if low_val not in self.Node_values:
            self.Node_values.append(low_val)
            self.Nodes[low_val] = self.Node(low_val)
            self.Nodes[low_val].Next.append(self.Nodes[high_val])
        else:
            self.Nodes[low_val].Next.append(self.Nodes[high_val])
    
    def is_path(self, node_1: Node, node_2: Node, _unvisited: list[Node] = [], _visited: list[Node]= []) -> bool:
        visited   = _visited
        visited.append(node_1)
        unvisited = _unvisited[1:] 
          
        for node in node_1.Next:
            if node not in visited:
                unvisited.append(node)

        if node_1 in node_2.Next:
            return False
        elif node_2 in node_1.Next:
            return True
        elif len(unvisited) == 0:
            return False
    
        return self.is_path(unvisited[0], node_2, unvisited, visited)
    
    def fix_path(self, node_1: Node, node_2: Node, _unvisited: list[Node] = [], _visited: list[Node]= []) -> tuple[Node, Node]:
        visited   = _visited
        visited.append(node_1)
        unvisited = _unvisited[1:] 
          
        for node in node_1.Next:
            if node not in visited:
                unvisited.append(node)

        if node_1 in node_2.Next:
            return (node_1, node_2)
        elif node_2 in node_1.Next:
            return None
        elif len(unvisited) == 0:
            return None
    
        return self.is_path(unvisited[0], node_2, unvisited, visited)


def part_one():
    data_file = open("05\\input.txt").read()
    data_rules, data_updates = data_file.split("\n\n")
    ret_val = 0

    #: Cleanup
    data_rules   = data_rules.split("\n")
    data_updates = [d for d in data_updates.split("\n")]
    data_updates = [d.split(",") for d in data_updates]

    #: Make graph
    graph = Graph()
    for rule in data_rules:
        low_val, high_val  = rule.split("|")
        graph.add_rule(low_val, high_val)

    #: validate array 
    for page in data_updates:
        failed = False
        for page_rule_index in range(len(page)-1):
            base_node = graph.Nodes[page[page_rule_index]]
            next_node = graph.Nodes[page[page_rule_index+1]]
            if not graph.is_path(base_node, next_node):
                failed = True
                break #: page failed
        ret_val = ret_val + int(page[int((len(page)-1)/2)]) if not failed else ret_val
    return ret_val


def part_two():
    data_file = open("05\\input.txt").read()
    data_rules, data_updates = data_file.split("\n\n")
    ret_val = 0

    #: Cleanup
    data_rules   = data_rules.split("\n")
    data_updates = [d for d in data_updates.split("\n")]
    data_updates = [d.split(",") for d in data_updates]

    #: Make graph
    graph = Graph()
    for rule in data_rules:
        low_val, high_val  = rule.split("|")
        graph.add_rule(low_val, high_val)

    #: validate array 
    for page in data_updates:
        fixed = False
        counter = 0
        while counter < len(page)-1:
            base_node = graph.Nodes[page[counter]]
            next_node = graph.Nodes[page[counter+1]]
            fixed_nodes = graph.fix_path(base_node, next_node)
            if fixed_nodes:
                fixed = True
                temp = page[counter]
                page[counter]   = page[counter+1]
                page[counter+1] = temp
                counter = -1
            counter += 1 
        ret_val = ret_val + int(page[int((len(page)-1)/2)]) if fixed else ret_val
    return ret_val


if __name__ == "__main__":
    start_time = time.time()
    print(f"result is: {part_one()}")
    print(f"Solved part one in: {time.time()-start_time} Seconds")

    start_time = time.time()
    print(f"result is: {part_two()}")
    print(f"Solved in: {time.time()-start_time} Seconds")