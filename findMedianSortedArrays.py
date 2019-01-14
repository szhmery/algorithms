class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        half = len(nums1) // 2
        print(half)
        print(nums1[half])
        print(nums1[~half])
        return (nums1[half] + nums1[~half]) / 2

    def findMedianSortedArrays2(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = int(half_len - i)-1
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0



# A1=[2,3,4,5]
# A2=[4,5,6,7]
A1=[1,2]
A2=[4,5,6,7]
s = Solution()
print(s.findMedianSortedArrays(A1,A2))
print(s.findMedianSortedArrays2(A1,A2))
