# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        count = 0
        for i, v in enumerate(s):
            count = count-1
            if s[i] != s[count]:
                return False

        return True

teste = Solution.isPalindrome(0)
print(teste)