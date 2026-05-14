# https://leetcode.com/problems/roman-to-integer/description/

romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        if len(s.strip()) == 0:
            return 0

        string = s.upper()
        lista_inteiro = []

        for i in range(len(string)):
            if string[i] in romanos:

                puxar_valor = True
                numero_atual = romanos[string[i]]
                proximo_numero = romanos[string[i + 1]] if i+1 < len(string) else 0

                if numero_atual < proximo_numero:
                    puxar_valor = False
                    string = string.replace(string[i + 1], 'N')
                    subtracao = proximo_numero - numero_atual
                    lista_inteiro.append(subtracao)

                if puxar_valor:
                    lista_inteiro.append(romanos[string[i]])

        return sum(lista_inteiro)

teste = Solution.romanToInt('MCMXCIV')
