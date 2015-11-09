#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
	size = 0
	N = len(A)

	for i, v in enumerate(A):
		if size == 0: #new candidate
			value = v
			size += 1
			index = i
		elif value == v: #same element
			size += 1
			index = i
		else: #delete pair
			size -= 1

	if size > 0: #has candidate
		count = 0
		for v in A:
			if v == value:
				count += 1
		if count > N // 2: #has dominator
			leader = value
		else:
			return 0
	else:
		return 0
	
	#print 'leader:',leader
	#print 'count:' ,count
	number = 0
	total_l_leader = 0
	for i, v in enumerate(A):
		if (v == leader):
			total_l_leader += 1
		total_l = i + 1
		total_r = N - total_l
		total_r_leader = count - total_l_leader

		#print 'total_l_leader:',total_l_leader
		#print 'total_l:',total_l
		#print 'total_r_leader:',total_r_leader
		#print 'total_r:',total_r
		if (total_l_leader > total_l//2 and total_r_leader > total_r//2):
			number += 1
		#print 'number', number	
		
	return number

A = [4, 3, 4, 4, 4, 2]
print solution(A)


"""
 zero-indexed array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
A[0] = 3    A[1] = 4    A[2] =  3
A[3] = 2    A[4] = 3    A[5] = -1
A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given a zero-indexed array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

For example, given array A such that
A[0] = 3    A[1] = 4    A[2] =  3
A[3] = 2    A[4] = 3    A[5] = -1
A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

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
0.067 s
OK
collapse all
Correctness tests
▶
single
single element
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
▶
double
two elements
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
▶
simple
simple test
✔
OK
1.
0.065 s
OK
2.
0.066 s
OK
▶
small_random
small random test with two values, length = ~100
✔
OK
1.
0.067 s
OK
▶
small
random + 200 * [MIN_INT] + random ,length = ~300
✔
OK
1.
0.066 s
OK
collapse all
Performance tests
▶
large_random
large random test with two values, length = ~50,000
✔
OK
1.
0.127 s
OK
▶
large
random(0,1) + 50000 * [0] + random(0, 1), length = ~100,000
✔
OK
1.
0.177 s
OK
▶
large_range
1, 2, ..., N, length = ~100,000
✔
OK
1.
0.161 s
OK
2.
0.066 s
OK
▶
extreme_large
all the same values
✔
OK
1.
0.202 s
OK

"""
