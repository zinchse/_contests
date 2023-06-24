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

    def time_to_sec(time) -> int:
        h, m, s = map(int, time.split(':'))
        return h * 60 * 60 + m * 60 + s

    # initialization
    N = int(input())
    morning, lunch_start, lunch_end, evening = map(time_to_sec, ['09:00:00', '13:00:00', '14:00:00', '18:00:00'])
    nails = [0 for _ in range(evening - morning + 1)]
    speeds = [0 for _ in range(evening - morning + 1)]
    prev_speed, prev_time = 0, 0

    # read schedule
    for i in range(N):
        cur_time_str, cur_speed_str = input().strip().split()
        cur_time = time_to_sec(cur_time_str) - morning
        cur_speed = int(cur_speed_str)
        for j in range(prev_time, cur_time):
            speeds[j] = prev_speed
        prev_time, prev_speed = cur_time, cur_speed
    for j in range(prev_time, evening - morning + 1):
        speeds[j] = prev_speed

    # before lunch
    if speeds[0] <= lunch_start - morning:
        nails[speeds[0]] = max(nails[speeds[0]], nails[0] + 1)
    for i in range(1, lunch_start - morning + 1):
        nails[i] = max(nails[i], nails[i - 1])
        if i + speeds[i] <= lunch_start - morning:
            nails[i + speeds[i]] = max(nails[i + speeds[i]], nails[i] + 1)

    # after lunch
    nails[lunch_end - morning] = nails[lunch_start - morning]
    for i in range(lunch_end - morning, evening - morning + 1):
        nails[i] = max(nails[i], nails[i - 1])
        if i + speeds[i] <= evening - morning:
            nails[i + speeds[i]] = max(nails[i + speeds[i]], nails[i] + 1)

    print(nails[-1])


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
