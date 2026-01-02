#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2) )
        """l=[]
        for i in nums1:
            if i in nums2:
                l.append(i)
        return list(set(l))"""

#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution(object):
    def intersect(self, nums1, nums2):

        freq = {}
        result = []

        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result

        


