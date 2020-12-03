class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(num):
    root = n = Node()

    while num:
        val = num % 10
        num = num // 10
        n.next = Node(val)
        n = n.next
    return root.next


def addTwo(arr1, arr2):
    root = dummy = Node()
    carry = 0

    while carry or arr1 or arr2:
        v1, v2 = 0, 0
        if arr1:
            v1 = arr1.val
            arr1 = arr1.next

        if arr2:
            v2 = arr2.val
            arr2 = arr2.next

        carry, quot = divmod(carry+v1+v2, 10)
        dummy.next = Node(quot)
        dummy = dummy.next
    return root.next


l1 = createList(342)
l2 = createList(465)

res = addTwo(l1, l2)
print()
