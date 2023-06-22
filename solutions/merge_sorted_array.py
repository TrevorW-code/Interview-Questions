class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # get last index nums1
        last = m + n - 1

        # start merging, reverse
        while m > 0 and n > 0:
            # if last item in nums1 > nums2
            if nums1[m-1] > nums2[n-1]:
                # set last item to that
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                # otherwise, add other element
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n - 1, last - 1