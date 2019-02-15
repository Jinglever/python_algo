from array_queue import ArrayQueue
from typing import Optional


class CircleQueue(ArrayQueue):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self._len = 0

    def enqueue(self, data: object):
        """
        入队，无需移动数组元素
        :param data:
        :return:
        """
        # 检查队列是否已满
        # if (self._tail + 1) % self._capacity == self._head:
        #     return False
        if self._len == self._capacity:
            return False
        self._array[self._tail] = data
        self._tail = (self._tail + 1) % self._capacity
        self._len += 1
        return True

    def dequeue(self) -> Optional[object]:
        """
        出队
        :return:
        """
        # if self._head == self._tail:  # 说明队列空
        #     return None
        if self._len == 0:
            return None
        else:
            obj = self._array[self._head]
            self._head = (self._head + 1) % self._capacity
            self._len -= 1
            return obj



if __name__ == '__main__':
    """test"""
    queue = CircleQueue(3)
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
