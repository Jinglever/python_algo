"""
实现二叉查找树即相关算法
"""

from typing import Optional


class Node(object):
    """
    二叉树节点
    存储的值是整数
    """
    def __init__(self, data: int=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.data)

class BinarySearchTree(object):
    """
    二叉查找树
    树中的任意一个节点，其左子树中的每个节点的值，都要小于这个节点的值，
    而右子树节点的值都大于这个节点的值
    """
    def __init__(self):
        self.root = None # 根节点
        # self.height = 0 # 高度
        # self.depth = 0 # 深度
        self.count = 0 # 节点个数

    def __len__(self) -> int:
        return self.count

    def add(self, num: int):
        """
        添加一个整数作为节点
        :param num:
        :return:
        """
        if not self.root:
            self.root = Node(num)
        else:
            p = self.root
            while p:
                if num == p.data: # 不接受重复数字
                    return
                pp = p
                if num < p.data:
                    p = p.left
                else:
                    p = p.right
            if num < pp.data:
                pp.left = Node(num)
            else:
                pp.right = Node(num)

        self.count += 1

    def delete(self, num: int):
        """
        删除一个节点
        :param num:
        :return:
        """
        pp = None # 父节点
        p = self.root
        while p and p.data != num:
            pp = p
            if num < p.data:
                p = p.left
            else:
                p = p.right

        if not p: # 如果没找到，就返回
            return
        # 先考虑被删除节点右两个子节点的情况
        if p.left and p.right:
            min_p = p.right # 将要寻找右子树最小值
            min_pp = p # min_p的父节点
            while min_p.left:
                min_pp = min_p
                min_p = min_p.left
            p.data = min_p.data # 这里最巧妙的地方，将数据替换过来
            p = min_p # 后面就变成了删除min_p了，且min_p一定没有左子树
            pp = min_pp
        # 被删除节点是叶子节点或者仅有一个节点
        if p.left:
            child = p.left
        elif p.right:
            child = p.right
        else:
            child = None
        if not pp: # 删除的是根节点
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child
        self.count -= 1




    def preorder_print_c(self, p: Optional[Node]):
        """
        对指定的节点做前序遍历
        :param p:
        :return:
        """
        if p:
            print(' ' + repr(p), end='')
            self.preorder_print_c(p.left)
            self.preorder_print_c(p.right)

    def preorder_print(self):
        """
        前序遍历
        :return:
        """
        self.preorder_print_c(self.root)

    def inorder_print_c(self, p: Node):
        """
        对指定的节点做中序遍历
        :param p:
        :return:
        """
        if p:
            self.inorder_print_c(p.left)
            print(' ' + repr(p), end='')
            self.inorder_print_c(p.right)

    def inorder_print(self):
        """
        中序遍历
        :return:
        """
        self.inorder_print_c(self.root)

    def postorder_print_c(self, p: Node):
        """
        对指定的节点做后序遍历
        :param p:
        :return:
        """
        if p:
            self.postorder_print_c(p.left)
            self.postorder_print_c(p.right)
            print(' ' + repr(p), end='')

    def postorder_print(self):
        """
        中序遍历
        :return:
        """
        self.postorder_print_c(self.root)

    def find(self, num: int) -> Optional[Node]:
        """
        查找某个数字
        :param num:
        :return:
        """
        p = self.root
        while p:
            if p.data == num:
                return p
            elif num <= p.data:
                p = p.left
            else:
                p = p.right
        return None




if __name__ == '__main__':
    """ test """
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    bst.add(3)
    bst.add(8)
    bst.add(15)
    bst.add(18)
    bst.add(13)
    print('前序遍历：')
    bst.preorder_print();
    print('\n中序遍历：')
    bst.inorder_print();
    print('\n后序遍历：')
    bst.postorder_print();
    print('\n')
    print(bst.find(10))
    print(bst.find(3))
    print(bst.find(13))
    print(bst.find(11))
    bst.delete(10)
    bst.preorder_print();
    print('\n')
    bst.inorder_print();
    print('\n')
    bst.postorder_print();
    print('\n')
