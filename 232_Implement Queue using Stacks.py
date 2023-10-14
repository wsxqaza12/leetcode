class MyQueue(object):

    def __init__(self):
        self.content = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.content.insert(0, x)

    def pop(self):
        """
        :rtype: int
        """
        return self.content.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.content[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.content


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
