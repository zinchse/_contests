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


def solve():
    from collections import deque

    def from_infix_to_postfix() -> str:
        stack, cur_str, string = deque(), '', ''

        for s in input().strip():

            if s in map(str, range(0, 10)):
                cur_str = cur_str + s
                continue

            elif cur_str:
                string = string + ' ' + cur_str
                cur_str = ''

            if s == ' ':
                continue

            elif s == '*':
                while len(stack) and stack[-1] == '*':
                    string = string + ' ' + stack.pop()
                stack.append(s)

            elif s == '-' or s == '+':
                while len(stack) and stack[-1] in ['*', '-', '+']:
                    string = string + ' ' + stack.pop()
                stack.append(s)

            elif s == '(':
                stack.append(s)

            elif s == ')':
                while len(stack) and stack[-1] != '(':
                    string = string + ' ' + stack.pop()
                assert len(stack) >= 1
                stack.pop()

            else:
                assert False

        if cur_str:
            stack.append(cur_str)

        while len(stack):
            item = stack.pop()
            assert item != '('
            string = string + ' ' + item

        return string

    def from_postfix_to_answer(string: str):
        stack = deque()
        error = False
        for s in string.split():

            if s in ['+', '-', '*']:
                if len(stack) < 2:
                    error = True
                    break
                x = stack.pop()
                y = stack.pop()
                if y in ['+', '-', '*'] or x in ['+', '-', '*']:
                    error = True
                    break
                stack.append(eval(f"{y}{s}{x}"))
            else:
                stack.append(s)

        if not error and len(stack) == 1:
            print(stack.pop())
        else:
            assert False

    try:
        from_postfix_to_answer(from_infix_to_postfix())
    except AssertionError:
        print("WRONG")


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
