class Node():
    """Doubly linked node which stores an object"""

    def __init__(self, element, next_node=None, previous_node=None):
        # The underscores are to prevent overwriting the variables
        # if inherited and prevents access from outside of scope
        self.__element = element
        self.__next_node = next_node
        self.__previous_node = previous_node

    def get_element(self):
        """Returns the element stored in this node"""
        return self.__element

    def get_previous(self):
        """Returns the previous linked node"""
        return self.__previous_node

    def get_next(self):
        """Returns the next linked node"""
        return self.__next_node

    def set_element(self, element):
        """Sets the element stored in this node"""
        self.__element = element

    def set_previous(self, previous_node):
        """Sets the previous linked node"""
        self.__previous_node = previous_node

    def set_next(self, next_node):
        """Sets the next linked node"""
        self.__next_node = next_node

    def __repr__(self):
        return str((self.__element, self.get_next()))
