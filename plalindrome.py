from singly_linked_list import *


def is_palindrome(sl_list: SinglyLinkedList) -> bool:
    """
    检测单链表中的字符是否属于回文
    时间复杂度 O(n)  空间复杂度 O(1)
    :param sl_list:
    :return: True | False
    """
    if not sl_list._head._next:
        return True
    p_prev = None
    p_slow = sl_list._head  # 慢指针，步长为 1
    p_fast = sl_list._head  # 快指针，步长为 2
    while p_fast and p_fast._next:
        """
        当快指针到达末尾，慢指针恰好指在链表中间位置
        """
        p_fast = p_fast._next._next

        # 对慢指针走过的前半段链表做链表反转
        p_next = p_slow._next
        p_slow._next = p_prev
        p_prev = p_slow
        p_slow = p_next

    if p_fast:  # 说明字符串长度为奇数
        p_forward = p_slow._next  # 往前走指针
        p_backward = p_prev  # 往后走指针
        p_prev = p_slow
    else:  # 字符串长度为偶数
        p_forward = p_slow
        p_backward = p_prev
        p_prev = p_forward
    result = True
    while p_forward and p_backward:
        if result and p_forward.data != p_backward.data:
            result = False  # 不能提前跳出循环，因为需要将前面反转了的一半链表恢复回去
        p_forward = p_forward._next

        # 反转恢复
        p_next = p_backward._next
        p_backward._next = p_prev
        p_prev = p_backward
        p_backward = p_next

    return result


if __name__ == '__main__':
    """
    test
    """
    while True:
        string = input('请输入字符串：\n')
        sll = singly_linked_list(string)
        print(sll)
        if is_palindrome(sll):
            print('是回文')
        else:
            print('不是回文')
        print(sll)
        print('\n')
