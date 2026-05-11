from typing import Optional

l1 = [2, 4, 3]
l2 = [5, 6, 4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(lista1: Optional[ListNode], lista2: Optional[ListNode]) -> Optional[ListNode]:
        while lista1 or lista2:
            v1 = lista1.val if lista1 else 0
            v2 = lista2.val if lista2 else 0

            calculo_anterior = None
            carry = None

            lista_calculados = [int]
            calculo = v1+v2
            if calculo >= 10:
                carry = calculo//10

            if calculo_anterior:
                calculo += carry


            print(calculo)

            lista1 = lista1.next if lista1 else None
            lista2 = lista2.next if lista2 else None


    @staticmethod
    def create_node_list(lista: list[int]):
        anterior = None
        lista_completa = None

        for i, v in enumerate(lista):
            atual = ListNode(v)
            if anterior:
                anterior.next = atual
                anterior = atual
            else:
                lista_completa = atual
                anterior = atual

        return lista_completa


l1_list = Solution.create_node_list(l1)
l2_list = Solution.create_node_list(l2)

solucao = Solution.addTwoNumbers(l1_list, l2_list)
