"""
实现跳表
存储的是正整数
"""

from typing import Optional
import random


class Node(object):
    def __init__(self, value: Optional[int] = None):
        self.data = value
        self.forwards = []  #原始链的指针以及各层索引的指针都存在这里

    def __repr__(self):
        return '{data: %d; levels: %d}' % (self.data, len(self.forwards))


class SkipList(object):
    _MAX_LEVEL = 16  # 最大索引层数 第0层是原链

    def __init__(self):
        self.head = Node()
        self.head.forwards = [None] * self._MAX_LEVEL
        self.level_count = 1  # 当前层数
        self.length = 0

    def find(self, value: int) -> Optional[Node]:
        # 从高到底逐层查找
        p = self.head
        for i in range(self.level_count - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
            if p.forwards[0] and p.forwards[0].data == value:
                return p.forwards[0].data
        return None

    def insert(self, value: int):
        new_node = Node(value)
        # 随机level
        random_level = self._random_level()
        # 定位各层里插入的位置
        update = [self.head] * random_level
        p = self.head
        for i in range(self.level_count - 1, random_level - 2, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
        for i in range(random_level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
            update[i] = p
        # 插入
        for i in range(random_level):
            new_node.forwards.append(update[i].forwards[i])
            update[i].forwards[i] = new_node
        # 更新level_count
        if random_level > self.level_count:
            self.level_count = random_level
        self.length += 1

    def delete(self, value: int):
        # 定位各层需要做删除操作的位置
        update = [None] * self.level_count
        p = self.head
        for i in range(self.level_count - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
                update[i] = p
        # 执行删除操作
        if p.forwards[0] and p.forwards[0].data == value:
            self.length -= 1
            for i in range(self.level_count):
                if update[i]:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]
                else:
                    return

    def _random_level(self) -> int:
        """
        随机level
        :return:
        """
        level = 1
        for i in range(1, self._MAX_LEVEL):
            if random.random() < 0.5:
                level += 1
        return level

    def __repr__(self):
        lines = []
        for i in range(self.level_count):
            nodes = []
            p = self.head
            while p.forwards[i]:
                nodes.append(repr(p.forwards[i].data))
                p = p.forwards[i]
            lines.append('->'.join(nodes))
        return '{\n' + '\n'.join(lines) + '\n}\n'


if __name__ == '__main__':
    """test"""
    # insert
    l = SkipList()
    for i in range(1000):
        l.insert(i)
    print(l)
    for i in range(2, 6):
        l.insert(i)
    print(l)
    print(l.find(10))
    l.delete(3)
    print(l)
