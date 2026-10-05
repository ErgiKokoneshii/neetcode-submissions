class Node:
    def __init__(self, url: str) -> None:
        self.data: str = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = self.head
        self.length = 1
        self.forward_tabs = 0

    def visit(self, url: str) -> None:
        new_page = Node(url)
        self.tail.next = new_page
        new_page.prev = self.tail
        self.tail = new_page
        self.forward_tabs = 0
        self.length += 1

    def back(self, steps: int) -> str:
        counter = steps
        if counter > self.length:
            counter = self.length
        for _ in range(counter):
            if self.tail.prev:
                self.tail = self.tail.prev
                self.forward_tabs += 1
        return self.tail.data

    def forward(self, steps: int) -> str:
        counter = steps
        if counter > self.forward_tabs:
            counter = self.forward_tabs
        for _ in range(counter):
            if self.tail:
                self.tail = self.tail.next
                self.forward_tabs -= 1
        return self.tail.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)