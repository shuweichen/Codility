#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"



def solution(A):
    B = sorted(A)
    N = len (A)
    count = 1
    
    for i in xrange(N-1):
        if B[i] != B[i+1]:
            count+=1
    if N == 0:
        return 0
    else:
        return count


"""
Write a function

    def solution(A)

that, given a zero-indexed array A consisting of N integers, returns the number of distinct values in array A.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

For example, given array A consisting of six elements such that:
A[0] = 2    A[1] = 1    A[2] = 1
A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""

"""
Analysis
Detected time complexity:
O(N) or O(N*log(N))
collapse all
Example tests
▶
example1
example test, positive answer
✔
OK
1.
0.068 s
OK
collapse all
Correctness tests
▶
extreme_empty
empty sequence
✔
OK
1.
0.069 s
OK
▶
extreme_single
sequence of one element
✔
OK
1.
0.066 s
OK
2.
0.068 s
OK
▶
extreme_two_elems
sequence of three distinct elements
✔
OK
1.
0.068 s
OK
▶
extreme_one_value
sequence of 10 equal elements
✔
OK
1.
0.066 s
OK
▶
extreme_negative
sequence of negative elements, length=5
✔
OK
1.
0.065 s
OK
▶
extreme_big_values
sequence with big values, length=5
✔
OK
1.
0.069 s
OK
▶
medium1
chaotic sequence of value sfrom [0..1K], length=100
✔
OK
1.
0.074 s
OK
▶
medium2
chaotic sequence of value sfrom [0..1K], length=200
✔
OK
1.
0.065 s
OK
▶
medium3
chaotic sequence of values from [0..10], length=200
✔
OK
1.
0.071 s
OK
collapse all
Performance tests
▶
large1
chaotic sequence of values from [0..100K], length=10K
✔
OK
1.
0.084 s
OK
▶
large_random1
chaotic sequence of values from [-1M..1M], length=100K
✔
OK
1.
0.218 s
OK
▶
large_random2
another chaotic sequence of values from [-1M..1M], length=100K
✔
OK
1.
0.196 s
OK
"""

