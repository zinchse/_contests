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

    PRIORITY = {'!': 3,
                '&': 2,
                '|': 1,
                '^': 1,
                }

    UNARITY = {'!': 1,
               '&': 2,
               '|': 2,
               '^': 2,
               }

    INVERSE = {'1': '0',
               '0': '1',
               }

    def from_infix_to_postfix():
        stack, res = deque(), ''

        for s in input().strip():

            if s in ['0', '1']:
                res += ' ' + s

            elif s == ' ':
                pass

            elif s in PRIORITY.keys():
                while len(stack) and stack[-1] in PRIORITY.keys() and PRIORITY[stack[-1]] >= PRIORITY[s]:
                    res += ' ' + stack.pop()
                stack.append(s)

            elif s == '(':
                stack.append(s)

            elif s == ')':
                while len(stack) and stack[-1] != '(':
                    res += ' ' + stack.pop()
                assert len(stack) >= 1
                stack.pop()

            else:
                assert False

        while len(stack):
            item = stack.pop()
            assert item != '('
            res += ' ' + item

        return res

    def from_postfix_to_answer(string):
        stack = deque()
        for s in string.split():
            if s in PRIORITY.keys():
                assert len(stack) >= UNARITY[s]

                if UNARITY[s] == 2:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(str(eval(f"{y}{s}{x}")))

                elif UNARITY[s] == 1:
                    stack.append(INVERSE[stack.pop()])

            elif s in ['0', '1']:
                stack.append(s)

            else:
                assert False

        assert len(stack) == 1
        print(stack.pop())

    try:
        from_postfix_to_answer(from_infix_to_postfix())
    except AssertionError:
        print('WRONG')


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
