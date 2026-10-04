class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        val: int = -1
        dummy = self.head
        if index > self.length - 1:
            return val
        else:
            for _ in range(index):
                if dummy.next is not None:
                    dummy = dummy.next
            if dummy is not None:
                val = dummy.data
        return val

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
            self.length += 1
            return
        new_head.next = self.head
        self.head = new_head
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
            self.length += 1
            return 
        self.tail.next = new_tail
        self.tail = new_tail
        self.length += 1

    def remove(self, index: int) -> bool:
        if index > self.length - 1 or self.head is None:
            return False
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return True
        else:
            dummy = self.head
            for _ in range(index - 1):
                dummy = dummy.next
            if dummy.next == self.tail:
                self.tail = dummy
            dummy.next = dummy.next.next
            self.length -= 1
        return True
        
    def getValues(self) -> List[int]:
        res: list[int] = []
        for _ in range(self.length):
            if self.head:
                res.append(self.head.data)
            self.head = self.head.next
        return res