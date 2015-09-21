#!/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, P, Q):

	N = len(S)
	M = len(P)
	S = list(S)
	num_1 = [0] * (N + 1)
	num_2 = [0] * (N + 1)
	num_3 = [0] * (N + 1)
	ANS = [0] * M 

	for i in xrange(0, N):
		if S[i] == 'A':
			S[i] = 1
			num_1[i+1] = num_1[i] + 1
			num_2[i+1] = num_2[i]
			num_3[i+1] = num_3[i]
		elif S[i] == 'C':
			S[i] = 2
			num_1[i+1] = num_1[i]
			num_2[i+1] = num_2[i] + 1
			num_3[i+1] = num_3[i]
		elif S[i] == 'G':
			S[i] = 3
			num_1[i+1] = num_1[i]
			num_2[i+1] = num_2[i]
			num_3[i+1] = num_3[i] + 1
		elif S[i] == 'T':
			S[i] = 4
			num_1[i+1] = num_1[i]
			num_2[i+1] = num_2[i]
			num_3[i+1] = num_3[i]
## P1 = A0
	for i in xrange(0, M):
		start = P[i]
		end = Q[i]
		if start == end:
			ANS[i] = S[start]
			continue

		if S[start] == 1:
			ANS[i] = 1
		elif S[start] == 2:
			if num_1[end+1] - num_1[start] > 0:
				ANS[i] = 1
			else:
				ANS[i] = 2
		elif S[start] == 3:
			if num_1[end+1] - num_1[start] > 0:
				ANS[i] = 1
			elif num_2[end+1] - num_2[start] > 0: 
				ANS[i] = 2
			else:
				ANS[i] = 3
		elif S[start] == 4:
			if num_1[end+1] - num_1[start] > 0:
				ANS[i] = 1
			elif num_2[end+1] - num_2[start] > 0: 
				ANS[i] = 2
			elif num_3[end+1] - num_3[start] > 0: 
				ANS[i] = 3
			else:
				ANS[i] = 4
#print num_1
#print num_2
#print num_3
	return ANS
	

S = ['C', 'A', 'G', 'C', 'C', 'T', 'A']
P = [2, 5, 0]
Q = [4, 5, 6]

print solution(S, P, Q)



"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty zero-indexed string S consisting of N characters and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

        a Results structure (in C), or
        a vector of integers (in C++), or
        a Results record (in Pascal), or
        an array of integers (in any other programming language).

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Assume that:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.

Complexity:

        expected worst-case time complexity is O(N+M);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""


"""
Analysis
Detected time complexity:
O(N + M)
collapse all
Example tests
▶
example
example test
✔
OK
1.
0.071 s
OK
collapse all
Correctness tests
▶
extreme_sinlge
single character string
✔
OK
1.
0.071 s
OK
2.
0.070 s
OK
3.
0.074 s
OK
4.
0.073 s
OK
▶
extreme_double
double character string
✔
OK
1.
0.071 s
OK
2.
0.070 s
OK
3.
0.072 s
OK
4.
0.073 s
OK
▶
simple
simple tests
✔
OK
1.
0.072 s
OK
2.
0.071 s
OK
3.
0.072 s
OK
▶
small_length_string
small length simple string
✔
OK
1.
0.071 s
OK
▶
small_random
small random string, length = ~300
✔
OK
1.
0.072 s
OK
collapse all
Performance tests
▶
almost_all_same_letters
GGGGGG..??..GGGGGG..??..GGGGGG
✔
OK
1.
0.252 s
OK
2.
0.116 s
OK
▶
large_random
large random string, length
✔
OK
1.
0.362 s
OK
▶
extreme_large
all max ranges
✔
OK
1.
0.348 s
OK

"""
