from __future__ import annotations

import os.path
import sys

INTO_FILE = False
output = []


def fast_input(file_name):
    global INTO_FILE
    if os.path.isfile(file_name):
        INTO_FILE = True
        with open(file_name, 'r') as file:
            input_lines = file.readlines()
    else:
        INTO_FILE = False
        input_lines = sys.stdin.readlines()

    for line in input_lines:
        yield line


fast_input_reader = fast_input('input.txt')


def input():
    return fast_input_reader.__next__()


def print(line):
    output.append(str(line))


# Idea:
# Let's implement our queue on singly linked lists, with support for the "insert in the middle" operation.
# I've modified my already written queue with timeslots. It might seem like an overkill,
# but the idea of the solution should be clear

def solve():
    from typing import TypeVar, Literal, List, Iterable

    Value = TypeVar("Value")

    class Node:
        def __init__(self,
                     value: Value | None = None):
            self._value: Value | None = value
            self._next: Node | None = None
            self._prev: Node | None = None

        def get_next(self) -> Node:
            return self._next

        def get_prev(self) -> Node:
            return self._prev

        def get_value(self):
            return self._value

        def set_prev(self, node: Node | None):
            self._prev = node

        def set_next(self, node: Node | None):
            self._next = node

    class Queue:
        def __init__(self, items: Iterable[Value] = ()):
            self._front: Node | None = None
            self._back: Node | None = None
            self._mid: Node | None = None
            self._mid_pos: int | None = None
            self._size: int = 0
            for item in items:
                self.push(item)

        def push(self, value: Value) -> Literal["ok"]:
            node = Node(value=value)
            if self._back is not None:
                self._back.set_next(node)
                self._back = node
            else:
                # don't forget about `mid` elem
                self._front = self._back = self._mid = node
                self._mid_pos = 0
            self._size += 1
            return "ok"

        def push_mid(self, value: Value) -> Literal["ok"]:
            # front
            if self._mid_pos is None:
                self._mid_pos = 0
                self._size = 1
                self._front = self._back = self._mid = Node(value=value)
                return "ok"

            # inside
            while self._mid_pos != (self._size - 1) // 2:
                self._mid = self._mid.get_next()
                self._mid_pos += 1
            node = Node(value=value)
            node.set_next(self._mid.get_next())
            self._mid.set_next(node)
            self._size += 1

            # end
            if node.get_next() is None:
                self._back = node

            return "ok"

        def pop(self) -> Value | Literal["error"]:
            if self._front is None:
                return "error"
            elif self._front is self._back:
                value = self._front.get_value()
                # don't forget about `mid` elem
                self._front = self._back = self._mid = None
                self._mid_pos = None
                assert self._size == 1, "Warning: wrong size value!"
                self._size = 0
                return value
            else:
                value = self._front.get_value()
                # don't forget about `mid` elem
                if self._mid_pos == 0:
                    self._mid = self._front.get_next()
                else:
                    self._mid_pos -= 1
                self._front = self._front.get_next()
                self._size -= 1
                return value

        def top(self) -> Value | Literal["error"]:
            if self._front is not None:
                return self._front.get_value()
            return "error"

        def clear(self) -> Literal["ok"]:
            while self._size:
                self.pop()
            return "ok"

        def get_size(self) -> int:
            return self._size

        def get_all_values(self) -> List[Value]:
            cur_node = self._front
            res = []
            while cur_node is not None:
                res.append(cur_node.get_value())
                cur_node = cur_node.get_next()
            return res

        def __str__(self) -> str:
            return self.get_all_values().__str__()

        def __getitem__(self, i: int) -> Value:
            if i < 0:
                i = self._size + i
            assert 0 <= i < self._size, f"Warning: wrong index value!"
            idx = 0
            cur_node = self._front
            while idx != i:
                cur_node = cur_node.get_next()
                idx += 1
            return cur_node.get_value()

    N = int(input())
    q = Queue()
    res = []
    for _ in range(N):
        commands = input().strip().split()
        if commands[0] == '-':
            res.append(q.pop())
        elif commands[0] == '*':
            q.push_mid(commands[1])
        else:
            q.push(commands[1])
    print('\n'.join(res))


def main():
    solve()
    answer = '\n'.join(output) + '\n'

    if INTO_FILE:
        with open('output.txt', 'w') as output_file:
            output_file.write(answer)
    else:
        sys.stdout.write(answer)


if __name__ == '__main__':
    main()
