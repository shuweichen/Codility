#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):

	D = B / K - A / K

	if A % K == 0:
		return D + 1
	else:
		return D

K = 4
A = 7
B = 9


print solution(A, B, K)



"""
Write a function:

    int solution(int A, int B, int K);

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

Complexity:

        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).

"""


"""
Analysis
Detected time complexity:
O(1)
collapse all
Example tests
▶
example
A = 6, B = 11, K = 2
✔
OK
1.
0.065 s
OK
collapse all
Correctness tests
▶
simple
A = 11, B = 345, K = 17
✔
OK
1.
0.064 s
OK
▶
minimal
A = B in {0,1}, K = 11
✔
OK
1.
0.065 s
OK
2.
0.064 s
OK
▶
extreme_ifempty
A = 10, B = 10, K in {5,7,20}
✔
OK
1.
0.064 s
OK
2.
0.064 s
OK
3.
0.064 s
OK
▶
extreme_endpoints
verify handling of range endpoints, multiple runs
✔
OK
1.
0.063 s
OK
2.
0.064 s
OK
3.
0.064 s
OK
4.
0.064 s
OK
5.
0.064 s
OK
6.
0.064 s
OK
collapse all
Performance tests
▶
big_values
A = 100, B=123M+, K=2
✔
OK
1.
0.064 s
OK
▶
big_values2
A = 101, B = 123M+, K = 10K
✔
OK
1.
0.064 s
OK
▶
big_values3
A = 0, B = MAXINT, K in {1,MAXINT}
✔
OK
1.
0.065 s
OK
2.
0.065 s
OK
▶
big_values4
A, B, K in {1,MAXINT}
✔
OK
1.
0.065 s
OK
2.
0.065 s
OK
3.
0.064 s
OK
4.
0.064 s
OK
"""

