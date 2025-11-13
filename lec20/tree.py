#node can be implemented using class
#only one root node or empty
#leaf nodes are dead-end nodes (no children), point to null or None
#sibling - shares same parent node
#binary tree: maximum 2 children for each node - sometimes 2, sometimes 1, sometimes 0
#binary tree: each node's data is greater than all in its left subtree
#binary tree: each node's data is less than all in its right subtree
#python SortedSet implements a binary search tree

from typing import Optional, TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            raise NotImplementedError
        return self.data.__eq__(other.data)

    def __str__(self) -> str:
        value: str = f'{self.data}'
        if self.left is not None:
            value += f' {self.left}'
        else:
            value += '  *'
        if self.right is not None:
            value += f' {self.right}'
        else:
            value += '  *'
        return f'({value})'

class Tree(Generic[T]):
    def __init__(self, root_data: Optional[T] = None) -> None:
        if root_data is None:
            self.root: Optional[Node[T]] = None
        else:
            self.root = Node[T](root_data)

    def __str__(self) -> str:
        return self.root.__str__()

    def __contains__(self, item: T) -> bool:
        return self.contains(item, self.root)

    #DFS (Depth-First Search) explores deep paths first
    def contains(self, item: T, node: Optional[Node[T]]) -> bool:
        if node is None:
            return False
        elif node.data == item:
            return True
        else:
            return self.contains(item, node.left) or self.contains(item, node.right)

tree: Tree[str] = Tree[str]('Entry way')

assert tree.root is not None
tree.root.left = Node[str]('Living room')

tree.root.left.right = Node[str]('Kitchen')

print('Kitchen' in tree)  # True
print('Bathroom' in tree)  # False

print(tree)  # (Entry way (Living room  * (Kitchen  *  *))  *)
