import sys
sys.path.append("/workspaces/factorNCI/refactorNCI/refactornci")
from refactornci.node import Node
from dll import DoublyLinkedList


class TestDoublyLinkedList:

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.size() == 0
        assert dll.is_empty() is True

    def test_repr(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_first(node1)
        assert repr(dll) == repr(node1)

    def test_iterator(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.add_first(node1)
        dll.add_after(node2, node1)
        elements = [node.get_element() for node in dll]
        assert elements == [1, 2]

    def test_map(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.add_first(node1)
        dll.add_after(node2, node1)
        dll.map(lambda x: x * 2)
        assert node1.get_element() == 2
        assert node2.get_element() == 4

    def test_get_first(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_first(node1)
        assert dll.get_first() == node1

    def test_get_last(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_last(node1)
        assert dll.get_last() == node1

    def test_get_previous(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_first(node1)
        assert dll.get_previous(node1) is dll._DoublyLinkedList__header

    def test_get_next(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_first(node1)
        assert dll.get_next(node1) is dll._DoublyLinkedList__trailer

    def test_add_before(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.add_first(node1)
        dll.add_before(node2, node1)
        assert node2.get_next() == node1
        assert node1.get_previous() == node2
        assert dll.size() == 2

    def test_add_after(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.add_first(node1)
        dll.add_after(node2, node1)
        assert node2.get_previous() == node1
        assert node1.get_next() == node2
        assert dll.size() == 2

    def test_add_first(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_first(node1)
        assert dll.get_first() == node1
        assert dll.size() == 1
        assert dll.is_empty() is False

    def test_add_last(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        dll.add_last(node1)
        assert dll.get_last() == node1
        assert dll.size() == 1
        assert dll.is_empty() is False

    def test_remove(self):
        dll = DoublyLinkedList()
        node1 = Node(1)
        node2 = Node(2)
        dll.add_first(node1)
        dll.add_after(node2, node1)
        dll.remove(node1)
        assert dll.size() == 1
        assert node1.get_next() is None
        assert node1.get_previous() is None
        assert node2.get_next() is dll._DoublyLinkedList__trailer
        assert node2.get_previous() is dll._DoublyLinkedList__header
