# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(string: str) -> int:
        vistos = {}
        string_fim = []
        lista_caracteres = []
        caracteres = ""
        novo_inicio = 0
        finalizar = True
        while finalizar:
            for i, v in enumerate(string, novo_inicio):
                if v in vistos:
                    lista_caracteres.append(caracteres)
                    caracteres = ""
                    novo_inicio = vistos[v] - 2
                    vistos.clear()
                else:
                    caracteres = caracteres+v

                string_fim.append(v)
                if len(string_fim) == len(string):
                    lista_caracteres.append(caracteres)
                    finalizar = False

                vistos[v] = i

        maior_lista = max(lista_caracteres, key=len)
        print(maior_lista)
        return len(maior_lista)

teste = Solution.lengthOfLongestSubstring('dvdf')
print(f'resultado: {teste}')