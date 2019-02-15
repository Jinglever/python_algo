from my_array import MyArray
from typing import Optional


class ArrayQueue(object):
    """
    用array来实现简单的单向顺序队列（先入先出）
    入队操作可能会需要移动数组元素
    """
    def __init__(self, capacity: int):
        self._array = MyArray(capacity)
        self._capacity = capacity
        self._head = 0  # 队头
        self._tail = 0  # 队尾

    def enqueue(self, data: object) -> bool:
        """
        从队尾入队
        :param data:
        :return:
        """
        # 检查队列是否已满
        if self._tail == self._capacity:
            if self._head == 0:  # 说明队列已满
                return False
            else:
                # 移动数组元素，腾出空间
                for i in range(self._head, self._tail):
                    self._array[i - self._head] = self._array[i]
                self._tail -= self._head
                self._head = 0
        self._array[self._tail] = data
        self._tail += 1
        return True

    def dequeue(self) -> Optional[object]:
        """
        出队
        :return:
        """
        if self._head == self._tail:  # 说明队列空
            return None
        else:
            self._head += 1
            return self._array[self._head - 1]

    def __iter__(self):
        for i in range(self._head, self._tail):
            yield self._array[i]

    def __repr__(self):
        nums = ['array(']
        for i in range(0, self._capacity):
            nums.append('  {} => {},'.format(i, repr(self._array[i])))
        nums.append(')')
        return '\n'.join(nums)


if __name__ == '__main__':
    """test"""
    queue = ArrayQueue(3)
    print(queue)
    queue.dequeue()
    queue.enqueue('a')
    print(queue)
    queue.enqueue('b')
    print(queue)
    queue.enqueue('c')
    print(queue)
    queue.enqueue('e')
    print(queue)
    queue.dequeue()
    print(queue)
    queue.enqueue('e')
    print(queue)
