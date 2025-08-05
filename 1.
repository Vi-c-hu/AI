import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty_tile = self.board.index(0)

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

    def manhattan_distance(self):
        distance = 0
        for i, value in enumerate(self.board):
            if value == 0:
                continue
            x, y = i % 3, i // 3
            goal_x, goal_y = (value - 1) % 3, (value - 1) // 3
            distance += abs(x - goal_x) + abs(y - goal_y)
        return distance

    def is_goal(self):
        return self.board == list(range(1, 9)) + [0]

    def neighbors(self):
        neighbors = []
        x, y = self.empty_tile % 3, self.empty_tile // 3
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_y * 3 + new_x
                new_board = self.board.copy()
                new_board[self.empty_tile], new_board[new_index] = new_board[new_index], new_board[self.empty_tile]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def path(self):
        current = self
        path = []
        while current:
            path.append(current.board)
            current = current.previous
        return path[::-1]

def solve_puzzle(start_board):
    start = PuzzleState(start_board)
    open_set = []
    heapq.heappush(open_set, start)
    visited = set()
    
    while open_set:
        current = heapq.heappop(open_set)
        if tuple(current.board) in visited:
            continue
        visited.add(tuple(current.board))

        if current.is_goal():
            return current.path()

        for neighbor in current.neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(open_set, neighbor)

    return None
start_board = [1, 2, 3,
               4, 0, 6,
               7, 5, 8]

solution = solve_puzzle(start_board)

if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found.")
