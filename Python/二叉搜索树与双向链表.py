# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        if  pRootOfTree.left == None  and pRootOfTree.right == None:
            # 这里只排除了左右子树都是空的情况，但是还要单独验证左右子树有一个为空
            return pRootOfTree
        left = self.Convert(pRootOfTree.left) # 这里的left是左子树构成的双向链表的的表头
        p = left
        while left and p.right:    # 因为left是头结点，因此需要定位到左子树的最后一个节点，和根节点建立左右节点关系
            p = p.right
        if left: # 如果根节点的左子树存在的话，与根节点建立关系
            p.right = pRootOfTree
            pRootOfTree.left = p    # 因为是双向链表，因此既要有左节点，又有右节点
        right = self.Convert(pRootOfTree.right) # 这里的right是右子树构成的双向链表的的表头，和左子树一样
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree
        return left if left else pRootOfTree  # 要是左子树存在的话，就返回left，否则不管右子树存不存在，根节点都是双向链表的头结点

