class MyLinkedList:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next = next
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.val = val
        else:
            dummy = MyLinkedList(self.val, self.next)
            self.val = val
            self.next = dummy
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
        cur = self
        while cur.next:
            cur = cur.next
        cur.next = MyLinkedList(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev = self
            for _ in range(index - 1):
                prev = prev.next
            prev.next = MyLinkedList(val, prev.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.next is None:
                self.val = 0
            else:
                self.val = self.next.val
                self.next = self.next.next
        else:
            prev = self
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
        self.size -= 1