"""
ou are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = 0
        self.next = next


def mergeTwo(l1, l2):
    dummy = res = Node()

    while l1 and l2:
        if l1.val < l2.val:
            res.next = l1
            l1 = l1.next
        else:
            res.next = l2
            l2 = l2.next
        res = res.next
    res.next = l1 or l2
    return dummy.next


def mergeKList(lists):
    n = len(lists)
    if n == 0:
        return None
    if n == 1:
        return lists[0]
    if n == 2:
        return mergeTwo(lists[0], lists[1])

    mid = n//2
    l, r = mergeKList(lists[:mid]), mergeKList(lists[mid:])
    return mergeTwo(l, r)
