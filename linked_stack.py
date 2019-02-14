"""
基于链表实现的栈
"""


class Node(object):
    def __init__(self, data: object, next_node=None):
        self._data = data
        self._next = next_node

    def __repr__(self):
        return repr(self._data)


class LinkedStack(object):
    """
    Simple Stack based on singly linked list
    """
    def __init__(self):
        self._top = None
        self.__len = 0

    def push(self, data: object):
        node = Node(data, self._top)
        self._top = node
        self.__len += 1

    def pop(self) -> object or None:
        if self._top:
            node = self._top
            self._top = node._next
            self.__len -= 1
            return node._data
        else:
            return None

    def __len__(self):
        return self.__len

    def __repr__(self):
        nums = []
        cur = self._top
        while cur:
            nums.append(repr(cur))
            cur = cur._next
        return '->'.join(nums)


if __name__ == '__main__':
    """test"""
    stack = LinkedStack()
    stack.push('a')
    stack.push(1)
    stack.push([4, 4, 4])
    print(stack)
    print('pop: {}'.format(stack.pop()))
    print('pop: {}'.format(stack.pop()))
    print(stack)

