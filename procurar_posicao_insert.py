# https://leetcode.com/problems/search-insert-position/description/


class Solution:
    @staticmethod
    def searchInsert(nums: list[int], target: int) -> float | int:
        esquerda = 0
        direita = len(nums) - 1

        while esquerda <= direita:
            meio = (esquerda+direita)//2
            if nums[meio] == target:
                return meio

            if nums[meio] > target:
                direita = meio-1

            else:
                esquerda = meio+1

            print(f'esquerda: {esquerda} | direita: {direita}')
        return esquerda

teste = Solution.searchInsert([1, 3, 5, 7, 9], 4)
print(teste)