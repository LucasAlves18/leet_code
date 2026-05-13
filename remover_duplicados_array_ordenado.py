# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    @staticmethod
    def removeDuplicates(nums: list[int]) -> int:
        k = 1
        for i, v in enumerate(nums[1:], 1):
            if v != nums[i - 1]:
                nums[k] = v
                k = k+1

        print(nums)
        return k

teste = Solution.removeDuplicates([1,2,3])
print(teste)