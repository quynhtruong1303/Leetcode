class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        currentString = []
        counts = []
        count = 0

        for c in s:
            if c in currentString:
                counts.append(count)
                index = currentString.index(c)
                currentString = currentString[(index+1):]
                count = len(currentString)
            count += 1
            currentString.append(c)
        counts.append(count)
        return max(counts) if counts else 0
        