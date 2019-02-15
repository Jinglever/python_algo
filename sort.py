"""
基于数组实现常见的排序算法
"""

from my_array import MyArray


def bubble_sort(array: MyArray, asc=True):
    """
    冒泡排序
    :param array: 成员可比较大小的MyArray
    :param asc: 是否升序 默认为True
    :return:
    """
    length = len(array)
    if length <= 1:
        return
    if asc:
        for i in range(length):
            swap = False
            for j in range(length - i -1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swap = True
            if not swap:
                break
    else:
        for i in range(length):
            swap = False
            for j in range(length - i -1):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swap = True
            if not swap:
                break


def insertion_sort(array: MyArray, asc=True):
    """
    插入排序
    :param array: 成员可比较大小的MyArray
    :param asc: 是否升序 默认为True
    :return:
    """
    length = len(array)
    if length <= 1:
        return
    if asc:
        for i in range(0, length):
            value = array[i]
            j = i - 1
            while j >= 0 and array[j] > value:
                array[j + 1] = array[j]  # 数据移动
                j -= 1
            array[j + 1] = value
    else:
        for i in range(0, length):
            value = array[i]
            j = i - 1
            while j >= 0 and array[j] < value:
                array[j + 1] = array[j]  # 数据移动
                j -= 1
            array[j + 1] = value


def selection_sort(array: MyArray, asc=True):
    """
    选择排序
    :param array: 成员可比较大小的MyArray
    :param asc: 是否升序 默认为True
    :return:
    """
    length = len(array)
    if length <= 1:
        return
    if asc:
        for i in range(0, length):
            hit = i
            for j in range(i+1, length):
                if data[j] < data[hit]:
                    hit = j
            data[i], data[hit] = data[hit], data[i]
    else:
        for i in range(0, length):
            hit = i
            for j in range(i+1, length):
                if data[j] > data[hit]:
                    hit = j
            data[i], data[hit] = data[hit], data[i]


if __name__ == '__main__':
    """test"""
    nums = [2, 5, 7, 1, 3, 8, 3, 4, 6]
    data = MyArray(9)
    for k in range(len(nums)):
        data[k] = nums[k]

    # bubble_sort(data, True)
    # print(data)
    # bubble_sort(data, False)
    # print(data)

    # insertion_sort(data, True)
    # print(data)
    # insertion_sort(data, False)
    # print(data)

    selection_sort(data, True)
    print(data)
    selection_sort(data, False)
    print(data)

