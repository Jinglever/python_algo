"""
基于数组实现常见的排序算法
"""

import random
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


def _merge(array: MyArray, start: int, end: int, pivot: int, asc=True):
    """
    合并
    :param array:
    :param start:
    :param end:
    :param pivot:
    :param asc:
    :return:
    """
    tmp_array = MyArray(end-start+1)  # 为了保证是稳定排序，空间复杂度是O(n)
    m = start
    n = pivot + 1
    i = 0
    if asc:
        while m <= pivot and n <= end:
            if array[m] < array[n]:
                tmp_array[i] = array[m]
                m += 1
            else:
                tmp_array[i] = array[n]
                n += 1
            i += 1
    else:
        while m <= pivot and n <= end:
            if array[m] > array[n]:
                tmp_array[i] = array[m]
                m += 1
            else:
                tmp_array[i] = array[n]
                n += 1
            i += 1
    if m <= pivot:
        for j in range(m, pivot + 1):
            tmp_array[i] = array[j]
            i += 1
    else:
        for j in range(n, end + 1):
            tmp_array[i] = array[j]
            i += 1

    for i in range(len(tmp_array)):
        array[i+start] = tmp_array[i]



def _merge_sort(array: MyArray, start: int, end: int, asc=True):
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
    pivot = (start + end) // 2
    # 分治递归
    _merge_sort(array, start, pivot, asc)
    _merge_sort(array, pivot + 1, end, asc)
    # 合并排序
    _merge(array, start, end, pivot, asc)


def merge_sort(array: MyArray, asc=True):
    """
    归并排序
    递归
    稳定排序  非原地排序 空间复杂度O(n) 时间复杂度O(nlogn)
    :param array:
    :param asc:
    :return:
    """
    _merge_sort(array, 0, len(array) - 1, asc)


def _partition(array: MyArray, start: int, end: int, asc=True) -> int:
    """
    对数组给定的范围随机选择一个元素作为分区点，并完成快排分区
    :param array:
    :param start:
    :param end:
    :param asc:
    :return:
    """
    # 随机选择一个位置的数值作为分区点
    pivot = random.randint(start, end)
    # 将这个分区点移到最右侧
    array[end], array[pivot] = array[pivot], array[end]
    pivot_value = array[end]
    i = start
    if asc:
        for j in range(start, end):
            if array[j] < pivot_value:
                if i != j:
                    # 将在pivot左侧的数据都移入已排序区
                    array[i], array[j] = array[j], array[i]
                i += 1  # i始终指向已排序区的下一个数据插入位置
    else:
        for j in range(start, end):
            if array[j] > pivot_value:
                if i != j:
                    # 将在pivot左侧的数据都移入已排序区
                    array[i], array[j] = array[j], array[i]
                i += 1  # i始终指向已排序区的下一个数据插入位置
    # 最后i所指向的位置一定就是pivot所在的位置
    array[i], array[end] = array[end], array[i]
    return i


def _quick_sort(array: MyArray, start: int, end: int, asc=True):
    """
    对指定区间做快速排序
    :param array:
    :param start:
    :param end:
    :param asc:
    :return:
    """
    # 递归停止条件
    if start >= end:
        return
    # 快排分区
    pivot = _partition(array, start, end, asc)
    # 分治递归
    _quick_sort(array, start, pivot-1, asc)
    _quick_sort(array, pivot+1, end, asc)


def quick_sort(array: MyArray, asc=True):
    """
    快速排序
    非稳定排序  原地排序  空间复杂度O(1)  时间复杂度O(nlogn)
    :param array:
    :param asc:
    :return:
    """
    _quick_sort(array, 0, len(array)-1, asc)


def _find_the_k_number(array:MyArray, k: int, start: int, end: int):
    """
    在指定的分区里寻找整个数组的第k大元素
    :param array:
    :param k:
    :param start:
    :param end:
    :return:
    """
    pivot = _partition(array, start, end, True)
    if pivot == k - 1:
        return array[pivot]
    if pivot >= k:  # 第k大的元素在左侧的分区里
        return _find_the_k_number(array, k, start, pivot-1)
    else:
        return _find_the_k_number(array, k, pivot+1, end)


def find_the_k_number(array: MyArray, k: int):
    """
    在O(n)的时间复杂度内求无序数组中的第k大元素
    利用了快排的分治和分区思想
    :param array:
    :param k:
    :return:
    """
    return _find_the_k_number(array, k, 0, len(array)-1)


def bucket_sort(array: MyArray, asc=True):
    """
    桶排序
    桶的个数约接近n，时间复杂度就越接近O(n)
    桶排序比较适合用在外部排序中。所谓的外部排序就是数据存储在外部磁盘中，
    数据量比较大，内存有限，无法将数据全部加载到内存中。
    :param array: 要求 array 的元素都是 0~9的数字
    :param asc:
    :return:
    """
    # 分成 0~2 3~5 6~8 9~10 4个桶
    buckets = {
        2: [],  # 0~2
        5: [],  # 3~5
        8: [],  # 6~8
        10: [], # 9~10
    }
    # 塞入桶中
    for i in range(len(array)):
        for upper, bucket in buckets.items():
            if array[i] <= upper:
                bucket.append(array[i])
                break
    # 每个桶快排
    if asc:
        j = 0
        for bucket in buckets.values():
            quick_sort(bucket, asc)
            for i in range(len(bucket)):
                array[j] = bucket[i]
                j += 1
    else:
        j = len(array) - 1
        for bucket in buckets.values():
            quick_sort(bucket, asc)
            for i in range(len(bucket)-1, -1, -1):
                array[j] = bucket[i]
                j -= 1



def counting_sort(array: MyArray, asc=True):
    """
    计数排序
    把数据划分成k个桶，每个桶的数据值都是相同的，省掉桶内排序的时间
    :param array: 要求数据是范围不大的数值 数值范围在0~9
    :param asc:
    :return:
    """
    # 遍历数组，得到每个桶的数值数量
    index_array = MyArray(10)
    for i in range(10):
        index_array[i] = 0
    for i in range(len(array)):
        index_array[array[i]] += 1
    # 对这个数组顺序求和
    if asc:
        for i in range(1, 10):
            index_array[i] += index_array[i-1]
    else:
        for i in range(8, -1, -1):
            index_array[i] += index_array[i+1]

    sorted_array = MyArray(len(array))
    # 扫描array，通过index_array定位到插入的位置
    for i in range(len(array)):
        sorted_array[index_array[array[i]] - 1] = array[i]
        index_array[array[i]] -= 1
    for i in range(len(sorted_array)):
        array[i] = sorted_array[i]




if __name__ == '__main__':
    """test"""
    nums = [2, 5, 7, 1, 3, 8, 3, 4, 6]
    data = MyArray(9)
    for k in range(len(nums)):
        data[k] = nums[k]
    print(data)

    # 冒泡排序
    # bubble_sort(data, True)
    # print(data)
    # bubble_sort(data, False)
    # print(data)

    # 插入排序
    # insertion_sort(data, True)
    # print(data)
    # insertion_sort(data, False)
    # print(data)

    # 选择排序
    # selection_sort(data, True)
    # print(data)
    # selection_sort(data, False)
    # print(data)

    # 归并排序
    # merge_sort(data, True)
    # print(data)
    # merge_sort(data, False)
    # print(data)

    # 快速排序
    # quick_sort(data, True)
    # print(data)
    # quick_sort(data, False)
    # print(data)

    # 无序数组中第k大元素
    # k = 1
    # print('第 {} 大的元素是 {}'.format(k, find_the_k_number(data, k)))
    # quick_sort(data, True)
    # print(data)

    # 桶排序
    # bucket_sort(data, True)
    # print(data)
    # bucket_sort(data, False)
    # print(data)

    # 计数排序
    counting_sort(data, True)
    print(data)
    counting_sort(data, False)
    print(data)

