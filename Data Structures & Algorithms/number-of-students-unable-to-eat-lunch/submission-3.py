from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = 0
        queue = deque(students)
        while sandwiches and sandwiches[0] in queue:
            if len(queue) > 0:
                if queue[0] == sandwiches[0]:
                    queue.popleft()
                    del sandwiches[0]
                else:
                    queue.append(queue.popleft())
        res = len(sandwiches)
        return res