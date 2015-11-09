#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def solution(A, B):
	count = 0
	R = []

	for i, v in enumerate(B):
		if v == 0 and not R: # first must alive fish
			count += 1
		elif v == 1: # find downstream fish
			R.append(A[i])
		elif v == 0: # fish meet
			while R and R[-1] < A[i]:
				R.pop()
			if not R:
				count += 1

	count += len(R)

	print R

	return count


A = [4,3,2,1,5]
B = [0,1,0,0,0]
print solution(A, B)


"""
You are given two non-empty zero-indexed arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

        0 represents a fish flowing upstream,
        1 represents a fish flowing downstream.

If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

        If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
        If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.

We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:
  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0

Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

    def solution(A, B)

that, given two non-empty zero-indexed arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [0..1,000,000,000];
        each element of array B is an integer that can have one of the following values: 0, 1;
        the elements of A are all distinct.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).


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
expand all
Correctness tests
▶
extreme_small
1 or 2 fishes
✔
OK
1.
0.067 s
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
0.068 s
OK
6.
0.068 s
OK
7.
0.068 s
OK
▶
simple1
simple test
✔
OK
▶
simple2
simple test
✔
OK
▶
small_random
small random test, N = ~100
✔
OK
collapse all
Performance tests
▶
medium_random
small medium test, N = ~5,000
✔
OK
1.
0.077 s
OK
▶
large_random
large random test, N = ~100,000
✔
OK
1.
0.247 s
OK
▶
extreme_range1
all except one fish flowing in the same direction
✔
OK
1.
0.250 s
OK
2.
0.231 s
OK
▶
extreme_range2
all fish flowing in the same direction
✔
OK
1.
0.254 s
OK

"""
