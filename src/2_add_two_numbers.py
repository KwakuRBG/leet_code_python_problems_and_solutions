# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def unpack_values(list_node, values=None):
    if values is None:
        values = []
    if isinstance(list_node.next, ListNode):
        unpack_values(list_node.next, values)

    values.append(list_node.val)
    return values


def pack_values(node_list, ln=None):
    if ln is None:
        ln = ListNode()
    it = iter(node_list)
    ln.next = next(it)
    for nodes in it:
        ln.val = nodes
    return ln


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    lx = unpack_values(l1)
    ly = unpack_values(l2)
    list_nodes = map(sum, zip(lx, ly))

    return pack_values(list_nodes)


l3 = addTwoNumbers(
        l1=ListNode(2, ListNode(4, ListNode(3))),
        l2=ListNode(5, ListNode(6, ListNode(4)))
)
x = l3.val
y = l3.next
z = y.val
xx = y.next
print(x, y, z, xx)
