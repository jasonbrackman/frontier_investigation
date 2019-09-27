from __future__ import annotations
from typing import List, NamedTuple, Callable, Optional, TypeVar, Generic, Set
import random
import time

T = TypeVar("T")


class Location(NamedTuple):
    x: int
    y: int


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node]):
        self.state: T = state
        self.parent: Optional[Node] = parent


class Maze:
    def __init__(self, width: int, height: int, sparseness: float):
        self.width: int = width
        self.height: int = height
        self.sparsness: float = sparseness
        self.cells: List[List[chr]] = list()

        # start / Goal are at opposite extremes of the Maze
        self.start = Location(0, 0)
        self.goal = Location(self.width-1, self.height-1)

        self.create()

    def create(self) -> None:
        for w in range(self.width):
            self.cells.append(list())
            for h in range(self.height):
                block = "x" if random.random() <= self.sparsness else " "
                self.cells[w].append(block)

        self.cells[self.start.x][self.start.y] = "S"
        self.cells[self.goal.x][self.goal.y] = "G"

    def successors(self, location: Location):
        results = list()
        for i in range(-1, 2):
            for j in range(-1, 2):

                x_i = location.x+i if location.x+i >= 0 else 0
                x_i = x_i if x_i < self.width else self.width-1
                y_j = location.y+j if location.y+j >= 0 else 0
                y_j = y_j if y_j < self.height else self.height-1
                print(x_i, y_j)
                test = self.cells[x_i][y_j]
                if test != "x":
                    results.append(Location(x_i, y_j))

        return results

    def reached_goal(self, location: Location) -> bool:
        return location == self.goal

    def __repr__(self) -> str:
        buffer = ""
        for w in range(self.width):
            buffer += ''.join(self.cells[w])
            buffer += "\n"
        return buffer


class Stack(Generic[T]):
    """LIFO"""

    def __init__(self):
        self.__container = list()

    @property
    def empty(self):
        return len(self.__container) == 0

    def push(self, item):
        self.__container.append(item)

    def pop(self):
        return self.__container.pop()

    def __repr__(self):
        return repr(self.__container)


def dfs(start: Location, goal_test: Callable, successors: Callable, ):

    frontier: Stack[Node] = Stack()
    frontier.push(Node(start, parent=None))
    explored: Set = set()

    while not frontier.empty:
        current_position = frontier.pop()

        if goal_test(current_position.state) is True:
            return current_position

        for child in successors(current_position.state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, parent=current_position))

    return None


if __name__ == "__main__":
    m = Maze(4, 4, 0.4)
    print(m)

    t1 = time.perf_counter()

    solution = dfs(m.start, m.reached_goal, m.successors)

    results = [solution.state]
    node = solution.parent
    while node.parent is not None:
        node = node.parent
        results.append(node.state)
    t2 = time.perf_counter()

    for item in reversed(results):
        print(item)
        m.cells[item.x][item.y] = '*'
    print(m)

    print(f"Time to complete: {t2-t1}")



