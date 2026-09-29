class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not r:
            return True
        if p and r and p.val == r.val:
            return self.isSameTree(p.left, r.left) and self.isSameTree(p.right, r.right)
        else:
            return False