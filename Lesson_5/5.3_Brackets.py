#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"


def solution(S):
	N = len(S)
	R = []

	for i in S:
		if i == "(" or i == "[" or i == "{":
			R.append(i)
		elif i == ")" and R:
			if R[-1] == "(":
				R.pop()
		elif i == "]" and R:
			if R[-1] == "[":
				R.pop()
		elif i == "}" and R:
			if R[-1] == "{":
				R.pop()
		else:
			return 0
	print R

	if R:
		return 0
	else:
		return 1



S = "{[()()]}"
print solution(S)


"""
 string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

		S is empty;
		S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
		S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

	def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

		N is an integer within the range [0..200,000];
		string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Complexity:

		expected worst-case time complexity is O(N);
		expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

"""


"""
Analysis
Detected time complexity:
O(N)
collapse all
Example tests
▶
example1
example test 1
✔
OK
1.
0.066 s
OK
▶
example2
example test 2
✔
OK
1.
0.065 s
OK
collapse all
Correctness tests
▶
negative_match
invalid structures
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
4.
0.066 s
OK
5.
0.066 s
OK
▶
empty
empty string
✔
OK
1.
0.065 s
OK
▶
simple_grouped
simple grouped positive and negative test, length=22
✔
OK
1.
0.065 s
OK
2.
0.066 s
OK
3.
0.066 s
OK
4.
0.065 s
OK
5.
0.066 s
OK
collapse all
Performance tests
▶
large1
simple large positive test, 100K ('s followed by 100K )'s + )(
✔
OK
1.
0.101 s
OK
2.
0.065 s
OK
3.
0.069 s
OK
▶
large2
simple large negative test, 10K+1 ('s followed by 10K )'s + )( + ()
✔
OK
1.
0.069 s
OK
2.
0.066 s
OK
3.
0.065 s
OK
▶
large_full_ternary_tree
tree of the form T=(TTT) and depth 11, length=177K+
✔
OK
1.
0.098 s
OK
▶
multiple_full_binary_trees
sequence of full trees of the form T=(TT), depths [1..10..1], with/without some brackets at the end, length=49K+
✔
OK
1.
0.077 s
OK
2.
0.076 s
OK
3.
0.074 s
OK
4.
0.074 s
OK
5.
0.066 s
OK
▶
broad_tree_with_deep_paths
string of the form [TTT...T] of 300 T's, each T being '{{{...}}}' nested 200-fold, length=120K+
✔
OK
1.
0.089 s
OK
2.
0.090 s
OK


"""
