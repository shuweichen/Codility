#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):

	N = len(A)
	acc = 1
	count = 0
	start = 0

	for i in xrange(0, N-1):
		if A[i] == 0 and ~start:
			start = 1

		if (start):
			if A[i+1] != 0:
				count = count + acc
			else :
				acc += 1

	if count > 1000000000:
		return -1

	else:
		return count

A = [0,1,0,1,1]


print solution(A)



"""
A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

    int solution(int A[], int N);

that, given a non-empty zero-indexed array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

the function should return 5, as explained above.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

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
0.068 s
OK
collapse all
Correctness tests
▶
single
single element
✔
OK
1.
0.068 s
OK
2.
0.068 s
OK
▶
double
two elements
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
4.
0.067 s
OK
▶
simple
simple test
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
collapse all
Performance tests
▶
medium_random
random, length = ~10,000
✔
OK
1.
0.076 s
OK
▶
large_random
random, length = ~100,000
✔
OK
1.
0.154 s
OK
▶
large_big_answer
0..01..1, length = ~100,000
✔
OK
1.
0.152 s
OK
2.
0.126 s
OK
▶
large_alternate
0101..01, length = ~100,000
✔
OK
1.
0.158 s
OK
2.
0.146 s
OK
▶
large_extreme
large test with all 1s/0s, length = ~100,000
✔
OK
1.
0.152 s
OK
2.
0.145 s
OK
3.
0.157 s
OK
"""
