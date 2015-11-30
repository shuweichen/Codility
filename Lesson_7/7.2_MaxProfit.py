#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
	N = len(A)
	min_candidate = 200000
	max_candidate = 0
	return_value = 0

	for i in A:
		if i < min_candidate:
			min_candidate = i
		if i > min_candidate and i - min_candidate > return_value:
			max_candidate = i
			return_value = max_candidate - min_candidate
			
	return return_value

A = [23171, 21011, 21123,21366, 21013, 21367]

print solution(A)
#print type(A)
#print dir(A)


"""
A zero-indexed array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

    def solution(A)

that, given a zero-indexed array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:
  A[0] = 23171
"""

"""
nalysis summary

The solution obtained perfect score.
Analysis
Detected time complexity:
O(N)
collapse all
Example tests
▶
example
example, length=6
✔
OK
1.
0.067 s
OK
collapse all
Correctness tests
▶
simple_1
V-pattern sequence, length=7
✔
OK
1.
0.065 s
OK
▶
simple_desc
descending and ascending sequence, length=5
✔
OK
1.
0.065 s
OK
2.
0.066 s
OK
▶
simple_empty
empty and [0,200000] sequence
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
▶
two_hills
two increasing subsequences
✔
OK
1.
0.065 s
OK
▶
max_profit_after_max_and_before_min
max profit is after global maximum and before global minimum
✔
OK
1.
0.065 s
OK
collapse all
Performance tests
▶
medium_1
large value (99) followed by short V-pattern (values from [1..5]) repeated 100 times
✔
OK
1.
0.065 s
OK
▶
large_1
large value (99) followed by short pattern (values from [1..6]) repeated 10K times
✔
OK
1.
0.144 s
OK
▶
large_2
chaotic sequence of 200K values from [100K..120K], then 200K values from [0..100K]
✔
OK
1.
0.433 s
OK
▶
large_3
chaotic sequence of 200K values from [1..200K]
✔
OK
1.
0.256 s
OK

"""
