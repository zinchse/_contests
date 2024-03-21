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
    from collections import deque, defaultdict

    def validate(s: str) -> None:
        stack, tag = deque(), ''
        for char in s:
            tag += char
            # close tag
            if char == '>':
                # check the correctness of obtained tag
                assert tag != '>' and tag[0] == '<' and tag != '<>' and tag != '</>'
                # if it is closing tag
                if tag[1] == '/':
                    assert len(stack) and stack[-1] == '<' + tag[2:]
                    stack.pop()
                    tag = ''
                # if it is opening tag
                else:
                    stack.append(tag)
                    tag = ''
            # create tag
            elif char == '<':
                assert tag == '<'
            # check the closing tag
            elif char == '/':
                assert tag == '</'
            # if it is a normal letter, the tag should have opened
            else:
                assert tag[0] == '<'

        assert not len(stack)
        return

    s = input().strip()
    d = defaultdict(int)
    alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    for char in s:
        d[char] += 1

    need_to_check = set()

    for char in alphabet:
        if d[char] % 2 != 0:
            need_to_check.add(char)

    if d['/'] != d['<'] // 2:
        need_to_check.add('/')

    if d['<'] != d['>']:
        need_to_check.add('<')
        need_to_check.add('>')

    if d['<'] % 2 != 0:
        need_to_check.add('<')

    if d['>'] % 2 != 0:
        need_to_check.add('>')

    for i in range(len(s)):
        for c in need_to_check:
            new_s = s[:i] + c + s[i + 1:]
            try:
                validate(new_s)
                print(new_s)
                return
            except AssertionError:
                continue


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
