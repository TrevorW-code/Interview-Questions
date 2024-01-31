class MinStack:

    def __init__(self):
        self.vals = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        min_val = min(val, self.min_vals[-1] if self.min_vals else val)
        self.min_vals.append(min_val)

    def pop(self) -> None:
        self.vals.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]