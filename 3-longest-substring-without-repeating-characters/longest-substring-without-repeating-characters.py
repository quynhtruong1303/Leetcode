class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        ------------
        My code
        ------------

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
        '''

        charSet = set()
        left = 0
        count = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            count = max(count, right - left + 1)

        return count

        