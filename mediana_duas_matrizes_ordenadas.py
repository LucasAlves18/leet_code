# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        if len(s) == 0:
            return ''

        lista = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    lista.append(substring)

        maior = str(max(lista, key=len))
        return maior

teste = Solution.longestPalindrome('aab')
print(teste)
