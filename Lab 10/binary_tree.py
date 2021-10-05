# SYSC 2100 Winter 2021 Lab 10
# Last edited: Mar. 22, 2021

# An implementation of a binary tree.

from typing import Any


class BTNode:
    """A node in a binary tree."""

    def __init__(self, item):
        """Initialize this node's payload with item.

        The new node doesn't have any children.
        """
        self._item = item
        self._left = None
        self._right = None

    def get_item(self) -> Any:
        """Return this nodes's payload."""
        return self._item

    def set_item(self, item: Any) -> None:
        """Replace this node's payload with item."""
        self._item = item

    item = property(get_item, set_item)

    # Using 'BTNode' as a type annotation is the PEP 484 hack for handling
    # forward references. Starting with Python 3.10, we should be able to
    # use BTNode as a type annotation within the class.

    def get_left_child(self) -> 'BTNode':
        """Return the left child of this node."""
        return self._left

    def set_left_child(self, left_child: 'BTNode') -> None:
        """Replace the left child of this node with left_child."""
        self._left = left_child

    left = property(get_left_child, set_left_child)

    def get_right_child(self) -> 'BTNode':
        """Return the right child of this node."""
        return self._right

    def set_right_child(self, right_child: 'BTNode') -> None:
        """Replace the left child of this node with right_child."""
        self._right = right_child

    right = property(get_right_child, set_right_child)

    def insert_left(self, item: Any) -> None:
        """Insert a new node containing item as the left child of this node."""
        if self._left is None:
            self._left = BTNode(item)
        else:
            new_child = BTNode(item)
            new_child._left = self._left
            self._left = new_child

    def insert_right(self, item: Any) -> None:
        """Insert a new node containing item as the right child of this node."""
        if self._right is None:
            self._right = BTNode(item)
        else:
            new_child = BTNode(item)
            new_child._right = self._right
            self._right = new_child

    def size(self) -> int:
        """Return the number of nodes in this binary tree."""
        if self is None:
            return 0
        else:
            if self._left and self._right:
                return 1 + self._left.size() + self._right.size()
            elif self._left:
                return 1 + self._left.size()
            elif self._right:
                return 1 + self._right.size()
            else:
                return 1

    def count(self, item) -> int:
        """Return the number of occurrences of item in this binary tree."""
        if self is None:
            return 0

        elif self._item == item:
            if self._left and self._right:
                return 1 + self._left.count(item) + self._right.count(item)
            elif self._left:
                return 1 + self._left.count(item)
            elif self._right:
                return 1 + self._right.count(item)
            else:
                return 1

        else:
            if self._left and self._right:
                return self._left.count(item) + self._right.count(item)
            elif self._left:
                return self._left.count(item)
            elif self._right:
                return self._right.count(item)
            else:
                return 0


def build_binary_tree() -> BTNode:
    """Build the binary tree shown in Exercise 1 in the lab handout,
    and return the reference to the root node.
    """
    originalNode = BTNode(5)
    originalNode.insert_left(17)
    originalNode.insert_right(12)
    originalNode.insert_left(7)
    originalNode.get_left_child().insert_right(9)
    originalNode.get_right_child().insert_right(6)
    originalNode.get_right_child().get_right_child().insert_left(1)

    return originalNode


def build_full_binary_tree() -> BTNode:
    """Build the full binary tree shown in Exercise 2 in the lab handout,
    and return the reference to the root node.
    """
    originalNode = BTNode(5)
    originalNode.insert_left(17)
    originalNode.insert_right(6)
    originalNode.insert_left(7)
    originalNode.insert_right(12)
    originalNode.get_left_child().insert_right(9)
    originalNode.get_right_child().insert_left(3)

    return originalNode


def preorder_print(root: BTNode) -> None:
    """Print the binary tree rooted at root using a preorder traversal."""
    if root is not None:
        print(root.item)
        preorder_print(root.left)
        preorder_print(root.right)


def inorder_print(root: BTNode) -> None:
    """Print the binary tree rooted at root using an inorder traversal."""
    if root is not None:
        inorder_print(root.left)
        print(root.item)
        inorder_print(root.right)


def postorder_print(root: BTNode) -> None:
    """Print the binary tree rooted at root using a postorder traversal."""
    if root is not None:
        postorder_print(root.left)
        postorder_print(root.right)
        print(root.item)


def size(root: BTNode) -> int:
    """Return the number of nodes in the binary tree rooted at the node
    referred to by root.
    """
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)
