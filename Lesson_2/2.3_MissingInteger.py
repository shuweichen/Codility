#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
	n = len(A)
	loc = [0] * (n)
	count = 0
	
	for i in xrange(n):
		if A[i] < n + 1 and A[i] > 0:
			loc[A[i]-1] = 1
			#count += 1
#print loc
	for i in xrange(n):
		if loc[i] == 0:
			return i + 1
	return n + 1
#	if count == n:
#		return n + 1
#	else:
#		return 1
#A = [1]
A = [1,3,6,4,1,2]

print solution(A)



"""
Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2

the function should return 5.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

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
