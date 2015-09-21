#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
    N = len (A)
    #min_avg = min( (A[0] + A[1]) / 2, (A[0] + A[1] + A[2]) / 3)
    min_avg = (A[0] + A[1]) / 2.0
    min_idx = 0
    now_avg = 0.0
    
    
    for i in xrange(1,N-1):
        now_avg = (A[i] + A[i+1]) / 2.0
        if now_avg < min_avg:
            min_avg = now_avg
            min_idx = i           
    
    if N > 2:      
        for i in xrange(N-2):
            now_avg = (A[i] + A[i+1] + A[i+2]) / 3.0
            if now_avg < min_avg:
                min_avg = now_avg
                min_idx = i
                
    return min_idx


"""

 non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Assume that:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""

"""
Analysis
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
0.067 s
OK
collapse all
Correctness tests
▶
double_quadruple
two or four elements
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
3.
0.067 s
OK
4.
0.066 s
OK
▶
simple1
simple test, the best slice has length 3
✔
OK
1.
0.066 s
OK
2.
0.065 s
OK
▶
simple2
simple test, the best slice has length 3
✔
OK
1.
0.067 s
OK
▶
small_random
random, length = 100
✔
OK
1.
0.067 s
OK
▶
medium_range
increasing, decreasing (legth = ~100) and small functional
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
3.
0.067 s
OK
collapse all
Performance tests
▶
medium_random
random, N = ~700
✔
OK
1.
0.066 s
OK
▶
large_ones
numbers from -1 to 1, N = ~100,000
✔
OK
1.
0.168 s
OK
2.
0.143 s
OK
▶
large_random
random, N = ~100,000
✔
OK
1.
0.178 s
OK
▶
extreme_values
all maximal values, N = ~100,000
✔
OK
1.
0.184 s
OK
2.
0.181 s
OK
3.
0.175 s
OK
▶
large_sequence
many seqeneces, N = ~100,000
✔
OK
1.
0.168 s
OK
2.
0.142 s
OK

"""
