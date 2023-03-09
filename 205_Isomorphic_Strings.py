# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
#
# Example
# 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example
# 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example
# 3:
#
# Input: s = "paper", t = "title"
# Output: true


def isIsomorphic(s, t):

    # create pattern for string s
    pattern_s = ''
    n = 0
    for i in range(len(s)):

        if s[i] in s[:i]:
            pattern_s += str(pattern_s[s[:i].index(s[i])])
            continue

        # if s[i] != s[i-1]:
        n += 1

        pattern_s += str(n)

    print(pattern_s)


    # create pattern for string t
    pattern_t = ''
    n = 0
    for i in range(len(t)):


        if t[i] in t[:i]:
            pattern_t += str(pattern_t[t[:i].index(t[i])])
            continue

        # if t[i] != t[i - 1]:
        n += 1

        pattern_t += str(n)

    print(pattern_t)

    if pattern_s == pattern_t:
        return True

    return False


# s = "egg"
# t = "add"

# s = "paper"
# t = "title"

# s = "foo"
# t = "bar"

# s = "leet"
# t = "code"

# s = "badc"
# t = "baba"

print(isIsomorphic(s, t))
