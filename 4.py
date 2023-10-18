class LNode:
    def __init__(self, elm, next_=None):
        self.elem = elm
        self.next = next_


llist1 = LNode(1)
pnode = llist1
for i in range(2, 11):
    pnode.next = LNode(i)
    pnode = pnode.next
pnode = llist1
while pnode is not None:
    print(pnode.elem)
    pnode = pnode.next
