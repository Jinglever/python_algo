
class Node:
    def __init__(self, data: object, next_node=None):
        self.data = data
        self._next = None

    def __str__(self):
        return self.data.__str__()


class SinglyLinkedList:
    """
    单链表
    """
    def __init__(self, string: str):
        """
        将字符串转成单链表存储
        :param string:
        """
        if len(string) > 0:
            prev = Node(string[0])
            self._head = prev
            self._length = 1
            for i in range(1, len(string)):
                cur = Node(string[i])
                prev._next = cur
                prev = cur
                self._length += 1
        else:
            self._head = None
            self._length = 0

    def __str__(self):
        if self._head is None:
            return 'empty'
        else:
            if self.hasLoop():
                return 'Loop Exist'
            else:
                cur = self._head
                string = cur.__str__()
                while cur._next is not None:
                    cur = cur._next
                    string += ' -> ' + cur.__str__()
                return string

    def __len__(self):
        return self._length

    def __getitem__(self, index: int) -> object:
        if index >= self._length:
            raise IndexError
        else:
            cur = self._head
            for i in range(0, index):
                cur = cur._next
            return cur.data

    def hasLoop(self) -> bool:
        """
        检测是否有环
        :return:
        """
        if self._length == 0:
            return False
        slow = self._head
        fast = self._head
        while slow._next and fast._next and fast._next._next:
            slow = slow._next
            fast = fast._next._next
            if slow == fast:
                return True
        else:
            return False


if __name__ == '__main__':
    """
    test
    """
    sll = SinglyLinkedList('abc')
    print(sll)
