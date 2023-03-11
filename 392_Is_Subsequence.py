# https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false


def isSubsequence(s, t):

    sp = 0
    tp = 0

    while sp < len(s) and tp < len(t):

        if s[sp] == t[tp]:
            sp += 1

        tp += 1

    return len(s) == sp

s = "ab"
t = "baab"


print(isSubsequence(s, t))


