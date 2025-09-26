class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a     # ensure a is the smaller array

        # window initiate
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2    # mid of a
            j = half - (i + 1) - 1     # mid of b

            aLeft = a[i] if i >= 0 else float('-inf')
            aRight = a[i+1] if (i+1) < len(a) else float('inf')
            bLeft = b[j] if j >= 0 else float('-inf')
            bRight = b[j+1] if (j+1) < len(b) else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                #odd
                if total % 2:
                    return min(aRight, bRight)
                #even
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0
            elif aLeft > bLeft:     
                r = i - 1
            else:
                l = i + 1