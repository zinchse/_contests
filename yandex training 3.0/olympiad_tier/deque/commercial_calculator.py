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


# Idea
# At each step, add 2 elements with the minimum value
#
# Proof:

# In fact, we are given an array ``A = [a1 ... an]``, and we need to do ``N-1`` addition operations on it
# (the results of which are put back into the array). It is required to choose such a sequence of arguments for
# addition, so that the total cost of all additions is minimal.
#
# We shall say that array ``A`` dominates array ``B`` if the following holds:
# - The arrays ``A'' and ``B'' have the same length
# - After ordering the arrays, it is true that ``A[i] <= B[i]``.
#
# Then it is true that if ``A`` dominates ``B``, then ``total_sum(A) <= total_sum(B)``. Indeed, we can
# copy any sequence of additions over the array ``B``, making them on the corresponding indices of the array ``A``
# (the correspondence between array indices is made based on their ordering after ordering). Because of the second
# property of domination, we will not get a value at each step more than (the domination will continue on those elements
# which we add to the end as a result of intermediate additions), then the optimal solution for ``A`` is not worse than
# the solution for ``B''.
#
# Now we can prove that the greedy solution is correct. Suppose we have an array of ``A``, then the optimal solution,
# using the addition of ``arg1`` and ``arg2`` at the current step, has the following total cost
# ``total_sum(A | arg1, arg2) = (arg1 + arg2) * 0.05 + total_sum(A')``, where ``A'`` is obtained by removing from ``A``
# elements ``arg1, arg2``, and adding ``arg1 + arg2`` to the end of the element. Obviously, among all possible
# choices ``arg1, arg2`` obtained by the greedy strategy ``A`` will dominate
# over all other elements, so its second term in ``total_sum(A | arg1, arg2)`` is optimal. It is easy
# notice that the first term is the smaller the sum of ``arg1 + arg2``, that is, the two minimal elements minimize
# of the simultaneous one as well.
#
# It turns out that by acting greedily at each step, we do not miss the optimal solution. We may consider that we have
# justified the induction step (moving to an array of one less length). The basis is obvious.

def solve():
    import heapq

    N = int(input().strip())
    values = list(map(int, input().strip().split()))
    heapq.heapify(values)
    res = .0
    while len(values) != 1:
        x = heapq.heappop(values)
        y = heapq.heappop(values)
        s = x + y
        res += s * 0.05
        heapq.heappush(values, s)
    print(f"{res:.2f}")


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
