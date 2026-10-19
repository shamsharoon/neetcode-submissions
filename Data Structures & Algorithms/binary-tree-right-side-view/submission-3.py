# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        q = deque([(0, root)])
        while q:
            i, cur = q.popleft()
            if not cur: continue
            if i < len(levels):
                levels[i] = cur.val
            else:
                levels.append(cur.val)
            q.append((i+1, cur.left))
            q.append((i+1, cur.right))
        return levels