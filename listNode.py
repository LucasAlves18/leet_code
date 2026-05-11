from typing import Optional

l1 = [2,4,3]
l2 = [5,6,4,6]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(lista1: Optional[ListNode], lista2: Optional[ListNode]) -> Optional[ListNode]:
        while lista1 or lista2:
            if not lista1.val:
                lista1.val = 0

            if not lista2.val:
                lista2.al = 0

            print(lista1.val)
            lista1 = lista1.next

            print(lista2.val)
            lista2 = lista2.next

        pass

    @staticmethod
    def create_node_list(lista:list[int]):
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