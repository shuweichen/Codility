#/usr/bin/python
# -*- coding: utf-8 -*-

# you can use print for debugging purposes, e.g.
# print "this is a debug message"



def solution(S):
	N = len(S)
	count = 0

	for i in S:
		if i == "(":
			count += 1
		else:
			count -= 1
		if count < 0:
			return 0
	
	if count == 0:
		return 1
	else:
		return 0



S = "()"	
print solution(S)


"""
A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Assume that:

        N is an integer within the range [0..1,000,000];
        string S consists only of the characters "(" and/or ")".

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1) (not counting the storage required for input arguments).


"""


"""
nalysis
Detected time complexity:
O(N)
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
	▶
	example2
	example test2
	✔
	OK
	1.
	0.066 s
	OK
	collapse all
	Correctness tests
	▶
	negative_match
	invalid structure, but the number of parentheses matches
	✔
	OK
	1.
	0.067 s
	OK
	2.
	0.067 s
	OK
	▶
	empty
	empty string
	✔
	OK
	1.
	0.066 s
	OK
	▶
	simple_grouped
	simple grouped positive and negative test, length=22
	✔
	OK
	1.
	0.067 s
	OK
	2.
	0.067 s
	OK
	3.
	0.066 s
	OK
	▶
	small_random
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
	collapse all
	Performance tests
	▶
	large1
	simple large positive and negative test, 10K or 10K+1 ('s followed by 10K )'s
	✔
	OK
	1.
	0.068 s
	OK
	2.
	0.068 s
	OK
	3.
	0.067 s
	OK
	▶
	large_full_ternary_tree
	tree of the form T=(TTT) and depth 11, length=177K+
	✔
	OK
	1.
	0.083 s
	OK
	2.
	0.065 s
	OK
	▶
	multiple_full_binary_trees
	sequence of full trees of the form T=(TT), depths [1..10..1], with/without unmatched ')' at the end, length=49K+
	✔
	OK
	1.
	0.070 s
	OK
	2.
	0.071 s
	OK
	3.
	0.066 s
	OK
	▶
	broad_tree_with_deep_paths
	string of the form (TTT...T) of 300 T's, each T being '(((...)))' nested 200-fold, length=1 million
	✔
	OK
	1.
	0.143 s
	OK
	2.
	0.067 s
	OK

"""
