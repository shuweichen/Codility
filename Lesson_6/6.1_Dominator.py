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
			return index
		else:
			return -1
	else:
		return -1


A = [3, 4, 3, 2, 3, -1, 3, 3]
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
Analysis
Detected time complexity:
O(N) or O(N*log(N))
collapse all
Example tests
▶
example
example test
✔
OK
1.
0.066 s
OK
collapse all
Correctness tests
▶
small_nondominator
all different and all the same elements
✔
OK
1.
0.066 s
OK
2.
0.065 s
OK
▶
small_half_positions
half elements the same, and half + 1 elements the same
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
▶
small
small test
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
▶
small_pyramid
decreasing and plateau, small
✔
OK
1.
0.066 s
OK
▶
extreme_empty_and_single_item
empty and single element arrays
✔
OK
1.
0.066 s
OK
2.
0.065 s
OK
▶
extreme_half1
array with exactly N/2 values 1, N even + [0,0,1,1,1]
✔
OK
1.
0.066 s
OK
2.
0.067 s
OK
▶
extreme_half2
array with exactly floor(N/2) values 1, N odd + [0,0,1,1,1]
✔
OK
1.
0.067 s
OK
2.
0.066 s
OK
▶
extreme_half3
array with exactly ceil(N/2) values 1 + [0,0,1,1,1]
✔
OK
1.
0.066 s
OK
2.
0.066 s
OK
collapse all
Performance tests
▶
medium_pyramid
decreasing and plateau, medium
✔
OK
1.
0.076 s
OK
▶
large_pyramid
decreasing and plateau, large
✔
OK
1.
0.165 s
OK
▶
medium_random
random test with dominator, N = 10,000
✔
OK
1.
0.077 s
OK
▶
large_random
random test with dominator, N = 100,000
✔
OK
1.
0.169 s
OK


"""
