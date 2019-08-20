"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.temp = []



    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        for _ in range(len(self.stack)-1):
            self.top_ = self.stack.pop()
            self.temp.append(self.top_)
        a = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return a

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)

    param_2 = obj.pop()
    param_3 = obj.peek()
    param_3 = obj.peek()
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    1==1