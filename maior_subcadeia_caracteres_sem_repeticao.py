# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
from typing import Sized


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(string: str) -> Sized | int:
        vistos = {}
        inicio = 0
        maior = 0
        for i, v in enumerate(string):
            if v in vistos and vistos[v] >= inicio:
                inicio = vistos[v] + 1
            vistos[v] = i
            maior = max(maior, i - inicio + 1)

        return maior


teste = Solution.lengthOfLongestSubstring('anviaj')
