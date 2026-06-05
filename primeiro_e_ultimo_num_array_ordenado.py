# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    @staticmethod
    def searchRange(nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        ultimo_indice = Solution.find_first(nums, target)

        if ultimo_indice == -1:
            return [-1, -1]

        left = 0
        rigth = ultimo_indice
        result = -1

        while left <= rigth:

            meio = (left + rigth) // 2

            if nums[meio] == target:
                result = meio
                rigth = meio-1

            if nums[meio] > target:
                rigth = meio - 1

            if nums[meio] < target:
                left = meio + 1

        return [result, ultimo_indice]

    @staticmethod
    def find_first(nums: list[int], target: int) -> int:
        left = 0
        rigth = len(nums) -1
        result = -1

        while left <= rigth:
            meio = (left + rigth) // 2

            if nums[meio] == target:
                result = meio

            if nums[meio] > target:
                rigth = meio - 1

            else:
                left = meio + 1

        return result


teste = Solution.searchRange(nums=[1,1,1], target=1)
print(teste)
