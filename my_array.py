from typing import Optional
from typing import List

class MyArray(object):
    """
    Simple Array
    """
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._list = [None] * capacity

    def __getitem__(self, index: int) -> Optional[object]:
        return self._list[index]

    def __setitem__(self, index: int, value: Optional[object]):
        if 0 <= index < self._capacity:
            self._list[index] = value
        else:
            raise IndexError

    def __len__(self) -> int:
        return len(self._list)

    def __iter__(self):
        for item in self._list:
            yield item

    def __repr__(self):
        return repr(self._list)


def my_array(a: List) -> MyArray:
    """
    将list转成array
    :param a:
    :return:
    """
    array = MyArray(len(a))
    for i in range(len(a)):
        array[i] = a[i]
    return array


if __name__ == '__main__':
    """
    test
    """
    array = MyArray(10)
    array[1] = 2
    print(array[1])
    print(array[2])
    array[9] = 3
    print(array[-1])
    array[2] = 'a'
    print(array[2])

