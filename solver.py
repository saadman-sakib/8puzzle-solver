import copy
from helper_classes import Queue, Node

class Solver:
    def __init__(self, board):
        self.board = board
        self.result = None
        self.explored = set()
        self.terminal_state = [
            [None,1,2],
            [3,4,5],
            [6,7,8]
        ]

    def empty_index(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return (i,j)

    def available_moves(self, board):
        moves = []
        i,j = self.empty_index(board)

        try:
            new_board = copy.deepcopy(board)
            new_board[i][j] = board[i+1][j]
            new_board[i+1][j] = None
            moves.append((new_board,"DOWN"))
        except:
            pass

        try:
            if i == 0:
                raise Exeption
            new_board = copy.deepcopy(board)
            new_board[i][j] = board[i-1][j]
            new_board[i-1][j] = None
            moves.append((new_board,"UP"))
        except:
            pass

        try:
            new_board = copy.deepcopy(board)
            new_board[i][j] = board[i][j+1]
            new_board[i][j+1] = None
            moves.append((new_board,"RIGHT"))
        except:
            pass

        try:
            if j == 0:
                raise Exeption
            new_board = copy.deepcopy(board)
            new_board[i][j] = board[i][j-1]
            new_board[i][j-1] = None
            moves.append((new_board,"LEFT"))
        except:
            pass

        return moves

    def heuristic(self, node):
        h = 0
        for i in range(3):
            for j in range(3):
                if node.state[i][j] != self.terminal_state[i][j]:
                    h += 1
        return node.level + h

    def pretty_print(self, board):
        print("------")
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    print(" ", sep="|",end="|")
                else:
                    print(board[i][j], sep="|",end="|")
            print()
        print("------")

    def ending(self, node):
        actions = []
        states  = []
        while node.parent is not None:
            states.append(node.state)
            actions.append(node.action)
            node = node.parent
        states.reverse()
        actions.reverse()
        print("\n\n\n")
        print("Solution:")
        for state, action in zip(states,actions):
            print(action," =>")
            self.pretty_print(state)

    def in_explored(self, state):
        for node in self.explored:
            if node.state == state:
                return True
        return False

    def solve(self):
        print("Solving...")
        q = Queue()
        start = Node(parent=None,
        			 state=self.board,
        			 level=0,
        			 action=None)
        q.add(start)

        while True:
            q.queue.sort(key = lambda x:self.heuristic(x),reverse=False)
            node = q.remove()
            self.explored.add(node)

            if node.state == self.terminal_state:
                self.ending(node)
                return None

            for state, action in self.available_moves(node.state):
                if not(q.contains_state(state)) and not(self.in_explored(state)):
                    child = Node(parent=node, 
                                 state=state, 
                                 level=node.level+1, 
                                 action=action)
                    q.add(child)