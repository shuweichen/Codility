#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):

	N = len(A)
	CNT_L = [0] * N 
	CNT_R = [0] * N 

	for i in xrange(0, N):
		if i - A[i] < 0:
			CNT_L[0] += 1
		else:
			CNT_L[i - A[i]] += 1
		if i + A[i] > N-1:
			CNT_R[N-1] += 1
		else:
			CNT_R[i + A[i]] += 1
	
#print CNT_L
#print CNT_R
	acc = 0
	total = 0
	for i in xrange(0, N):
		acc += CNT_L[i]
		if acc == 0 or CNT_R[i] == 0:
			continue
#print 'acc' 
#print acc
		a0 = acc - 1
		an = acc - CNT_R[i]
		n = CNT_R[i]
		sn = (a0 + an) * n / 2
		
		total += sn
		if total > 10000000:
			return -1
#print 'sn'
#print sn
		acc -= CNT_R[i]
	
	return total
	

A = [1, 5, 2, 1, 4, 0]

print solution(A)



"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""


"""
Analysis
Detected time complexity:
O(N*log(N)) or O(N)
collapse all
Example tests
▶
example1
example test
✔
OK
1.
0.067 s
OK
collapse all
Correctness tests
▶
simple1
✔
OK
1.
0.066 s
OK
▶
simple2
✔
OK
1.
0.067 s
OK
2.
0.067 s
OK
▶
simple3
✔
OK
1.
0.066 s
OK
▶
extreme_small
empty and [10]
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
▶
small1
✔
OK
1.
0.067 s
OK
▶
small2
✔
OK
1.
0.067 s
OK
▶
small3
✔
OK
1.
0.066 s
OK
▶
overflow
arithmetic overflow tests
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
collapse all
Performance tests
▶
medium1
✔
OK
1.
0.069 s
OK
▶
medium2
✔
OK
1.
0.069 s
OK
▶
medium3
✔
OK
1.
0.074 s
OK
▶
medium4
✔
OK
1.
0.082 s
OK
▶
10M_intersections
10.000.000 intersections
✔
OK
1.
0.082 s
OK
▶
big1
✔
OK
1.
0.154 s
OK
2.
0.065 s
OK
▶
big2
✔
OK
1.
0.149 s
OK
2.
0.067 s
OK
▶
big3
[0]*50000
✔
OK
1.
0.139 s
OK
2.
0.067 s
OK
"""
