#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"



def solution(A):
    B = sorted(A)
    N = len (A)
    start = 0
    
    for i in xrange(N):
        if B[i] > 0:
            start = i
            break
    #print start
            
    for i in xrange(start, N-2):
        if B[i] + B[i+1] > B[i+2]:
            return 1
    
    return 0


"""
A zero-indexed array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given a zero-indexed array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""


"""
Analysis
Detected time complexity:
O(N*log(N))
collapse all
Example tests
▶
example
example, positive answer, length=6
✔
OK
1.
0.068 s
OK
▶
example1
example, answer is zero, length=4
✔
OK
1.
0.067 s
OK
collapse all
Correctness tests
▶
extreme_empty
empty sequence
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
3.
0.066 s
OK
4.
0.066 s
OK
5.
0.066 s
OK
▶
extreme_single
1-element sequence
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.066 s
OK
▶
extreme_two_elems
2-element sequence
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.066 s
OK
5.
0.066 s
OK
▶
extreme_negative1
three equal negative numbers
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.067 s
OK
▶
extreme_arith_overflow1
overflow test, 3 MAXINTs
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.066 s
OK
5.
0.066 s
OK
▶
extreme_arith_overflow2
overflow test, 10 and 2 MININTs
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
0.067 s
OK
5.
0.067 s
OK
▶
extreme_arith_overflow3
overflow test, 0 and 2 MAXINTs
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
4.
0.067 s
OK
5.
0.066 s
OK
▶
medium1
chaotic sequence of values from [0..100K], length=30
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
3.
0.067 s
OK
4.
0.066 s
OK
5.
0.067 s
OK
▶
medium2
chaotic sequence of values from [0..1K], length=50
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
5.
0.066 s
OK
▶
medium3
chaotic sequence of values from [0..1K], length=100
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.067 s
OK
collapse all
Performance tests
▶
large1
chaotic sequence with values from [0..100K], length=10K
✔
OK
1.
0.077 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.066 s
OK
5.
0.066 s
OK
▶
large2
1 followed by an ascending sequence of ~50K elements from [0..100K], length=~50K
✔
OK
1.
0.110 s
OK
2.
0.067 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.067 s
OK
▶
large_random
chaotic sequence of values from [0..1M], length=100K
✔
OK
1.
0.175 s
OK
2.
0.066 s
OK
3.
0.065 s
OK
4.
0.066 s
OK
5.
0.066 s
OK
▶
large_negative
chaotic sequence of negative values from [-1M..-1], length=100K
✔
OK
1.
0.197 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.066 s
OK
▶
large_negative2
chaotic sequence of negative values from [-10..-1], length=100K
✔
OK
1.
0.169 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.067 s
OK
▶
large_negative3
sequence of -1 value, length=100K
✔
OK
1.
0.157 s
OK
2.
0.067 s
OK
3.
0.066 s
OK
4.
0.067 s
OK
5.
0.065 s
OK

"""
