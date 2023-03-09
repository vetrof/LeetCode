
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """


        counts = {}

        for c in magazine:
            counts[c] = counts.get(c, 0) + 1

        print(counts )

        for c in ransomNote:
            if c not in counts or counts[c] == 0:
                return False

        #
            counts[c] -= 1
        print(counts)
        #
        # return True



ransomNote = "aa"
magazine = "aab"

print(Solution.canConstruct(0, ransomNote, magazine))