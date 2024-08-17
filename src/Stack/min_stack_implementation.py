"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""
class MinStack:

    stack = []
    min_stack = []
    index_top = -1
    def __init__(self):
        index_top = -1
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.index_top == -1:
            self.stack.append(val)
            self.min_stack.append(val)
            self.index_top += 1
            return
        self.stack.append(val)
        if self.min_stack[self.index_top] <= val:
            self.min_stack.append(self.min_stack[self.index_top])
            self.index_top += 1
        else:
            self.min_stack.append(val)
            self.index_top += 1

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        self.index_top -= 1

    def top(self) -> int:
        return self.stack[self.index_top]

    def getMin(self) -> int:
        return self.min_stack[self.index_top]


# Your MinStack object will be instantiated and called as such:
def solve():
    obj = MinStack()
    print(obj)
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj)
    param_1 = obj.getMin()
    print(param_1)
    obj.pop()
    print(obj)
    param_2 = obj.top()
    print(param_2)
    param_3 = obj.getMin()
    print(param_3)
