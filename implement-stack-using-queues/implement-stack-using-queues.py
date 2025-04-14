class MyStack:

    def __init__(self):
        self.queue = []
        self.rev_queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        while self.queue:
            self.rev_queue.append(self.queue.pop())

    def pop(self) -> int:
        return self.rev_queue.pop(-1)

    def top(self) -> int:
        return self.rev_queue[-1]

    def empty(self) -> bool:
        return not self.queue and not self.rev_queue