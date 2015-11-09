#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"



def solution(H):
	N = len(H)
	record = [H[0]]
	#record.append(H[0])
	count = 1

	for i in xrange(1, N):
		if (H[i] > H[i-1]):
			count += 1
			record.append(H[i])
		elif H[i] < H[i-1]:
#while H[i] < record[-1]:
			while record and H[i] < record[-1]:
				record.pop()
			if not record or H[i] != record[-1]:
				count += 1
				record.append(H[i])

		print "i: %d" %(i)
		print "count %d" %(count)
		print "record %s" %(record)
	return count

H = [8,8,5,7,9,8,7,4,8]	
print solution(H)


"""
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by a zero-indexed array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    int solution(int H[], int N);

that, given a zero-indexed array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

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
0.065 s
OK
▶
simple2
✔
OK
1.
0.067 s
OK
▶
simple3
✔
OK
1.
0.065 s
OK
▶
simple4
✔
OK
1.
0.065 s
OK
2.
0.065 s
OK
▶
boundary_cases
✔
OK
1.
0.066 s
OK
2.
0.065 s
OK
3.
0.066 s
OK
4.
0.065 s
OK
collapse all
Performance tests
▶
medium1
✔
OK
1.
0.065 s
OK
▶
medium2
✔
OK
1.
0.065 s
OK
▶
medium3
✔
OK
1.
0.066 s
OK
▶
medium4
✔
OK
1.
0.066 s
OK
▶
large_piramid
✔
OK
1.
0.178 s
OK
▶
large_increasing_decreasing
✔
OK
1.
0.164 s
OK
2.
0.190 s
OK
▶
large_up_to_20
✔
OK
1.
0.176 s
OK
▶
large_up_to_100
✔
OK
1.
0.179 s
OK
▶
large_max
✔
OK
1.
0.198 s
OK


"""
