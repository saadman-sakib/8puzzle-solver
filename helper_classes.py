class Node:
    """docstring for Move"""
    def __init__(self, parent, state, action, level):
        self.parent = parent
        self.action = action
        self.state = state
        self.level = level
        
class Queue:
    def __init__(self):
        self.queue = []
    
    def add(self, element):
        self.queue.append(element)

    def remove(self):
        node = self.queue[0]
        self.queue = self.queue[1:]
        return node

    def empty(self):
        return len(self.queue) == 0

    def contains_state(self, state):
        for move in self.queue:
            if move.state == state:
                return True
        return False