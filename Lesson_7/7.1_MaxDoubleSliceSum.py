#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
    N = len(A)
    sum_l = [0] * N
    sum_r = [0] * N

    for i in xrange(1, N-2):
        sum_l[i] = max(sum_l[i-1] + A[i], 0)

    for i in xrange(N-2, 1, -1):
        sum_r[i] = max(sum_r[i+1] + A[i], 0)
        #print sum_r[i]
    maximum = 0

    for i in xrange(1, N-1):
        maximum = max(sum_l[i-1] + sum_r[i+1], maximum)

    return maximum



A = [3, 2, 6, -1, 4, 5, -1, 2]

print solution(A)
#print type(A)
#print dir(A)



"""
A non-empty zero-indexed array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater than 17.

Assume that:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""

"""
nalysis
Detected time complexity:
O(N)
collapse all
Example tests
▶
example
example test
✔
OK
1.
0.069 s
OK
collapse all
Correctness tests
▶
simple1
first simple test
✔
OK
1.
0.068 s
OK
2.
0.067 s
OK
3.
0.067 s
OK
▶
simple2
second simple test
✔
OK
1.
0.068 s
OK
2.
0.066 s
OK
▶
simple3
third simple test
✔
OK
1.
0.067 s
OK
▶
negative
all negative numbers
✔
OK
1.
0.066 s
OK
▶
positive
all positive numbers
✔
OK
1.
0.066 s
OK
▶
extreme_triplet
three elements
✔
OK
1.
0.065 s
OK
collapse all
Performance tests
▶
small_random1
random, numbers form -10**4 to 10**4, length = 70
✔
OK
1.
0.066 s
OK
▶
small_random2
random, numbers from -30 to 30, length = 300
✔
OK
1.
0.066 s
OK
▶
medium_range
-1000, ..., 1000
✔
OK
1.
0.070 s
OK
▶
large_ones
random numbers from -1 to 1, length = ~100,000
✔
OK
1.
0.206 s
OK
▶
large_random
random, length = ~100,000
✔
OK
1.
0.229 s
OK
▶
extreme_maximal
all maximal values, length = ~100,000
✔
OK
1.
0.227 s
OK
▶
large_sequence
many the same small sequences, length = ~100,000
✔
OK
1.
0.199 s
OK
2.
0.206 s
OK

"""
