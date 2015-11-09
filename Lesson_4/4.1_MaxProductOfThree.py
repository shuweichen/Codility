#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"



def solution(A):
    N = len(A)
    A.sort()
    if A[0] >= 0 or A[N-1] < 0:
        return A[N-3]*A[N-2]*A[N-1]
    elif A[N-2]*A[N-3] > A[0]*A[1]:
        return A[N-3]*A[N-2]*A[N-1]
    else:
        return A[N-1]*A[0]*A[1]

print solution(A)


"""
A non-empty zero-indexed array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Assume that:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""


"""
Analysis
Detected time complexity:
O(N * log(N))
collapse all
Example tests
▶
example
example test
✔
OK
1.
0.065 s
OK
collapse all
Correctness tests
▶
one_triple
three elements
✔
OK
1.
0.066 s
OK
2.
0.065 s
OK
3.
0.065 s
OK
▶
simple1
simple tests
✔
OK
1.
0.065 s
OK
2.
0.065 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
▶
simple2
simple tests
✔
OK
1.
0.067 s
OK
2.
0.067 s
OK
3.
0.066 s
OK
▶
small_random
random small, length = 100
✔
OK
1.
0.067 s
OK
collapse all
Performance tests
▶
medium_range
-1000, -999, ... 1000, length = ~1,000
✔
OK
1.
0.067 s
OK
▶
medium_random
random medium, length = ~10,000
✔
OK
1.
0.075 s
OK
▶
large_random
random large, length = ~100,000
✔
OK
1.
0.177 s
OK
▶
large_range
2000 * (-10..10) + [-1000, 500, -1]
✔
OK
1.
0.107 s
OK
▶
extreme_large
(-2, .., -2, 1, .., 1) and (MAX_INT)..(MAX_INT), length = ~100,000
✔
OK
1.
0.138 s
OK
2.
0.149 s
OK

"""
