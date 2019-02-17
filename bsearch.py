"""
二分查找算法
"""
from my_array import MyArray, my_array


def bsearch(a: MyArray, n: int, target: int):
    """
    二分查找
    非递归实现
    :param a:  数组
    :param n:  数组大小
    :param target:  查找的对象
    :return:
    """
    low, high = 0, n-1
    while low <= high:  # 注意循环停止条件
        mid = low + (high - low >> 1)
        print('mid={}'.format(mid))  # debug
        if a[mid] == target:
            return mid
        elif a[mid] < target:  # 在右半区
            low = mid + 1  # 注意要+1
        else:
            high = mid - 1  # 注意要-1
    return None


def l_find(a: MyArray, n: int, target: int):
    """
    从左往右查找第一个值等于给定值的元素
    :param a:
    :param n:
    :param target:
    :return:
    """
    low, high = 0, n-1
    while low <= high:  # 注意循环停止条件
        mid = low + (high - low >> 1)
        print('mid={}'.format(mid))  # debug
        if a[mid] == target:
            # 找到后要往左遍历找到第一个
            for i in range(mid-1, low-1, -1):
                if a[i] != target:
                    return i + 1
            else:
                return low
        elif a[mid] < target:  # 在右半区
            low = mid + 1  # 注意要+1
        else:
            high = mid - 1  # 注意要-1
    return None


def r_find(a: MyArray, n: int, target: int):
    """
    从左往右查找最后一个值等于给定值的元素
    :param a:
    :param n:
    :param target:
    :return:
    """
    low, high = 0, n-1
    while low <= high:  # 注意循环停止条件
        mid = low + (high - low >> 1)
        print('mid={}'.format(mid))  # debug
        if a[mid] == target:
            # 找到后要往右遍历找到最后一个
            for i in range(mid+1, high+1):
                if a[i] != target:
                    return i - 1
            else:
                return high
        elif a[mid] < target:  # 在右半区
            low = mid + 1  # 注意要+1
        else:
            high = mid - 1  # 注意要-1
    return None


if __name__ == '__main__':
    """test"""
    # 有序的整数数组
    data = my_array([1,2, 2, 3, 3, 3, 4,5,6,7,8,9])
    print(data)

    # print(bsearch(data, len(data), 3))
    print(l_find(data, len(data), 8))
    print(r_find(data, len(data), 8))
