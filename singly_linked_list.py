
class Node(object):
    def __init__(self, data: object, next_node=None):
        self.data = data
        self._next = None

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList(object):
    """
    单链表
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self.__len = 0

    def append(self, data: object):
        """
        在末尾添加一个节点
        :param data:
        :return:
        """
        node = Node(data)
        if not self._head:
            self._tail = self._head = node
        else:
            self._tail._next = node
            self._tail = node
        self.__len += 1

    def __repr__(self):
        if self._head is None:
            return 'empty'
        else:
            if self.hasLoop():
                return 'Loop Exist'
            else:
                nums = []
                cur = self._head
                while cur:
                    nums.append(repr(cur))
                    cur = cur._next
                return '->'.join(nums)

    def __len__(self):
        return self.__len

    def __getitem__(self, index: int) -> object:
        if index >= self.__len:
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
        if self.__len == 0:
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

    def reserve(self):
        """
        翻转单向链表
        :return:
        """
        p, self._tail, prev = self._head, self._head, None
        while p._next:
            q, p._next = p._next, prev
            prev, p = p, q
        p._next, self._head = prev, p



def singly_linked_list(string: str) -> SinglyLinkedList:
    """
    将string转成单链表存储
    :param string:
    :return:
    """
    sl_list = SinglyLinkedList()
    if len(string) > 0:
        for i in range(0, len(string)):
            sl_list.append(string[i])
    return sl_list


if __name__ == '__main__':
    """
    test
    """
    sll = singly_linked_list('abcdef')
    print(repr(sll))
    sll.reserve();
    print(repr(sll))
