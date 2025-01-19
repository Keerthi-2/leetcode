class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Step 1: Initialize parent and current pointers
        parent = None
        current = root

        # Step 2: Find the node to delete and its parent
        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        # If the key is not found in the BST
        if not current:
            return root

        # Step 3: Handle the three cases of deletion

        # Case 1: Node to delete has no children (leaf node)
        if not current.left and not current.right:
            if not parent:  # If deleting the root node
                return None
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node to delete has one child
        elif not current.left or not current.right:
            child = current.left if current.left else current.right
            if not parent:  # If deleting the root node
                return child
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node to delete has two children
        else:
            # Find the inorder successor (minimum value in the right subtree)
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Replace current's value with the successor's value
            current.val = successor.val

            # Delete the successor node
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root
