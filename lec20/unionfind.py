#union-find algorithm finds disjoint sets
#helps with grouping/clustering
#combining two graphs is called union operation
#find determines which set an element belongs to / finds representative of the graph (root node)

from typing import TypeVar, Generic, Dict, Any
T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data:T) -> None:
        self.data:T = data
        self.parent: Node[T] = self
        self.rank: int = 0
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            if self.data==other.data and self.rank==other.rank:
                return True
        return False
    def __str__(self) -> str:
        return f"Node rank {self.rank}, with data {self.data}"

class UnionFind(Generic[T]):
    def __init__(self) -> None:
        self.nodes: Dict[T, Node[T]] = dict()

    def find(self, x:Node[T]) -> Node[T]:
        if x==x.parent:
            return x
        else:
            self.find(x.parent)

    def union(self, x:Node[T], y:Node[T]) -> None:
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return
        if root1.rank > root2.rank:
            root2.parent = root1
        else:
            root1.parent = root2
            if root1.rank == root2.rank:
                root2.rank+=1

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.parent = node2
node2.parent = node3
uf: UnionFind[int] = UnionFind()
found = uf.find(node1)
print(found)
