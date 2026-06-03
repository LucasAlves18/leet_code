# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    @staticmethod
    def searchRange(nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        indice_um = Solution.find_first(nums, target)

        return [indice_um, indice_um]

    @staticmethod
    def find_first(nums: list[int], target: int) -> int:
        left = 0
        rigth = len(nums) - 1

        while left <= rigth:
            meio = (left+rigth)//2

            if nums[meio] == target:
                return meio

            if nums[meio] > target:
                rigth = meio - 1

            else:
                left = meio + 1

        return -1

teste = Solution.searchRange(nums = [1], target = 0)
print(teste)
