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


    class LList:
        def __init__(self):
            self._head = None

        def is_empty(self):
            return self._head is None

        def prepend(self, elem):
            self._head = LNode(elem, self._head)

        def pop(self):
            if self._head is None:
                raise LinkedListUnderflow("in pop")
            e = self._head.elem
            self._head = self._head.next
            return e
