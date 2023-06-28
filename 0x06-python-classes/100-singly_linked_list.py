#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""defining a singly linked list in python using object oriented programming
"""


class Node:
    """a class Node that defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """attributes instantiation

        Args:
            data (int): data of the linked list
            next_node (class, optional): a node in the linked.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """method that retrieves the data attribute

        Returns:
            int: returns the set data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """method that sets the data attribute

        Args:
            value (value): value to be stored in the data

        Raises:
            TypeError: error if inserted value isn't an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """method at retrieves the next_node instance

        Returns:
            Node: returns a new node from the Node class
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """method that sets the new node

        Args:
            value (Node): new node value to be added to the linked list

        Raises:
            TypeError: raises an error if provided value parameter
            isn't a valid data type
        """
        if (value is not None) and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        """_summary_
        """
        self.head = None

    def sorted_insert(self, value):
        """creates an object of the class SinglyLinkedList

        Args:
            value (int): value of the linked list node
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """a method that helps return a string object

        Returns:
            string: returns the linked list value as a string
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
