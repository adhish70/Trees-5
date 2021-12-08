# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Logic: Start from the top. Connect left and right. When you move 
# to the next level, the previous level now has connection between 
# all the nodes in the above level.

# Time Complexity: O(n)
# Space Complexity: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:         
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        if root.left:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
        
        return root