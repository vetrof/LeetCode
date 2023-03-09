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

    index_symbol_in_t = -1
    for i in range(len(s)):
        if s[i] in t and t.index(s[i]) > index_symbol_in_t:
            index_symbol_in_t = t.index(s[i])
            continue

        else:
            return False

    return True


s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))


