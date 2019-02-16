"""
基于数组实现常见的排序算法
"""

from my_array import MyArray


def bubble_sort(array: MyArray, asc=True):
    """
    冒泡排序
    稳定排序  原地排序  平均时间复杂度O(n^2)
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
                if array[j] > array[j + 1]:  # 冒泡
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
    原地排序  稳定排序  平均时间复杂度O(n^2)
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
            while j >= 0 and array[j] > value:  # 找到在已排序区的插入位置
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
    原地排序  非稳定排序  平均时间复杂度O(n^2)
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
                if data[j] < data[hit]:  # 从未排序区选出候选人，排入已排序区末尾
                    hit = j
            data[i], data[hit] = data[hit], data[i]
    else:
        for i in range(0, length):
            hit = i
            for j in range(i+1, length):
                if data[j] > data[hit]:
                    hit = j
            data[i], data[hit] = data[hit], data[i]


def sub_merge_sort(array: MyArray, start: int, end: int, asc=True):
    """
    对指定区间的数据做归并排序
    :param array:
    :param start:
    :param end:
    :param asc:
    :return:
    """
    # 递归终止条件
    if start >= end:
        return
    # 取中间位置作为分区点
    position = (start + end) // 2
    # 分治递归
    sub_merge_sort(array, start, position, asc)
    sub_merge_sort(array, position+1, end, asc)
    # 合并排序
    tmp_array = MyArray(end-start+1)  # 为了保证是稳定排序，空间复杂度是O(n)
    m = start
    n = position + 1
    i = 0
    if asc:
        while m <= position and n <= end:
            if array[m] < array[n]:
                tmp_array[i] = array[m]
                m += 1
            else:
                tmp_array[i] = array[n]
                n += 1
            i += 1
    else:
        while m <= position and n <= end:
            if array[m] > array[n]:
                tmp_array[i] = array[m]
                m += 1
            else:
                tmp_array[i] = array[n]
                n += 1
            i += 1
    if m <= position:
        for j in range(m, position + 1):
            tmp_array[i] = array[j]
            i += 1
    else:
        for j in range(n, end + 1):
            tmp_array[i] = array[j]
            i += 1

    for i in range(len(tmp_array)):
        array[i+start] = tmp_array[i]


def merge_sort(array: MyArray, asc=True):
    """
    归并排序
    递归
    :param array:
    :param asc:
    :return:
    """
    sub_merge_sort(array, 0, len(array)-1, asc)



if __name__ == '__main__':
    """test"""
    nums = [2, 5, 7, 1, 3, 8, 3, 4, 6]
    data = MyArray(9)
    for k in range(len(nums)):
        data[k] = nums[k]
    # print(data)

    # bubble_sort(data, True)
    # print(data)
    # bubble_sort(data, False)
    # print(data)

    # insertion_sort(data, True)
    # print(data)
    # insertion_sort(data, False)
    # print(data)

    # selection_sort(data, True)
    # print(data)
    # selection_sort(data, False)
    # print(data)

    merge_sort(data, True)
    print(data)
    merge_sort(data, False)
    print(data)

