class Solution(object):
    def isSymmetrical(self, pRoot):
        """
        :type pRoot: TreeNode
        :rtype: bool
        """
        if pRoot == None:
            return True
        return self.checkTwoTree(pRoot.left,pRoot.right)
    def checkTwoTree(self, leftTree, rightTree):
        if leftTree==None and rightTree==None:
            return True
        if leftTree!=None and rightTree==None:
            return False
        if leftTree==None and rightTree!=None:
            return False
        if leftTree.val != rightTree.val:
            return False
        left = self.checkTwoTree(leftTree.left,rightTree.right)
        right = self.checkTwoTree(leftTree.right,rightTree.left)
        return left and right