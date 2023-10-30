import sys
sys.path.append("/factorNCI/refactorNCI/refactornci")
from refactornci.node import Node


class TestNode:

    def test_init(self):
        node = Node(42)
        assert node.get_element() == 42
        assert node.get_previous() is None
        assert node.get_next() is None

    def test_set_element(self):
        node = Node(42)
        node.set_element(10)
        assert node.get_element() == 10

    def test_set_previous(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.set_previous(node2)
        assert node1.get_previous() == node2

    def test_set_next(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.set_next(node2)
        assert node1.get_next() == node2

    def test_repr(self):
        node = Node(42)
        assert repr(node) == "(42, None)"
