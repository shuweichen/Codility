#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
	n = len(A)
	loc = [0] * (n)
	count = 0
	
	for i in xrange(n):
		if A[i] < n + 1:
			if loc[A[i]-1] == 0:
				count += 1
				loc[A[i]-1] = 1
			else:
				return 0
	if count == n:
		return 1
	else:
		return 0

A = [4,1,3,2]

print solution(A)



"""
 non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


"""


"""
nalysis
Detected time complexity:
O(N) or O(N * log(N))
expand all
Example tests
▶
example1
the first example test
✔
OK
▶
example2
the second example test
✔
OK
expand all
Correctness tests
▶
extreme_min_max
single element with minimal/maximal value
✔
OK
▶
single
single element
✔
OK
▶
double
two elements
✔
OK
▶
antiSum1
total sum is correct, but it is not a permutation, N <= 10
✔
OK
▶
small_permutation
permutation + one element occurs twice, N = ~100
✔
OK
expand all
Performance tests
▶
medium_permutation
permutation + few elements occur twice, N = ~10,000
✔
OK
▶
antiSum2
total sum is correct, but it is not a permutation, N = ~100,000
✔
OK
▶
large_permutation
permutation + one element occurs three times, N = ~100,000
✔
OK
▶
large_range
sequence 1, 2, ..., N, N = ~100,000
✔
OK
▶
extreme_values
all the same values, N = ~100,000 
"""
