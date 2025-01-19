class Solution:
    def deleteNode(self, A: Optional[TreeNode], B: int) -> Optional[TreeNode]:
        if not A:  # If the tree is empty, return None
            return None
        
        if B < A.val:  # If the target value is smaller, recurse on the left subtree
            A.left = self.deleteNode(A.left, B)
        elif B > A.val:  # If the target value is larger, recurse on the right subtree
            A.right = self.deleteNode(A.right, B)
        else:  # Found the node to delete
            if not A.left and not A.right:  # Case 1: Node has no children
                return None
            elif not A.left:  # Case 2: Node has only right child
                return A.right
            elif not A.right:  # Case 3: Node has only left child
                return A.left
            else:  # Case 4: Node has two children
                # Find the inorder predecessor (maximum value in the left subtree)
                temp = A.left
                prev = None
                while temp.right:
                    prev = temp
                    temp = temp.right
                
                # Replace A's value with the inorder predecessor's value
                A.val = temp.val
                
                # Delete the inorder predecessor node
                if prev:  # If the predecessor has a parent
                    prev.right = temp.left
                else:  # If the predecessor is the direct left child of A
                    A.left = temp.left
        
        return A
