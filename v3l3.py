import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def checkBalanced(root):
    def innerCheckBalanced(root):
        if root is None:
            return True, 0 # balanced, height
        leftB, leftH = innerCheckBalanced(root.left)
        rightB, rightH = innerCheckBalanced(root.right)

        H = max(leftH, rightH) + 1
        B = leftB and rightB and not(abs(leftH - rightH) > 1 and leftH!=0 and rightH!=0)
        return B, H # balanced, height
    
    return innerCheckBalanced(root)[0]


class TestCheckBalanced(unittest.TestCase):

    def test_balanced_tree(self):
        #     1
        #   /   \
        #  2     3
        # / \   /
        # 4   5 6
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        self.assertTrue(checkBalanced(root))

    def test_unbalanced_tree(self):
        #     1
        #   /   \
        #  2     3
        # /     /
        # 4    6
        # /
        # 5
        # \
        # 7
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(5)
        root.left.left.left.left = BinaryTree(7)
        root.right.left = BinaryTree(6)
        self.assertFalse(checkBalanced(root))

    def test_single_node(self):
        # 1
        root = BinaryTree(1)
        self.assertTrue(checkBalanced(root))

    def test_null_tree(self):
        # (empty tree)
        self.assertTrue(checkBalanced(None))

    def test_skewed_right_tree(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(3)
        self.assertTrue(checkBalanced(root))

    def test_skewed_left_tree(self):
        #     1
        #    /
        #   2
        #  /
        # 3
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        self.assertTrue(checkBalanced(root))

if __name__ == "__main__":
    unittest.main()