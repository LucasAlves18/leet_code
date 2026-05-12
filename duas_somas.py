"""
Calcular números de um array e retornar as posições
que o resultado da soma dão o valor de target
"""
# https://leetcode.com/problems/two-sum/

nums = [3, 2, 3]
target = 6

class Solution:
    @staticmethod
    def two_sum(num: list[int], alvo: int):
        visto = {}
        for i, v in enumerate(num):
            complemento = alvo - v
            if complemento in visto:
                return visto[complemento], i

            visto[v] = i

        return 'Nada deu certo bixo'

result = Solution.two_sum(nums, target)
print(result)
