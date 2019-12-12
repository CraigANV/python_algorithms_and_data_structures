#!/usr/bin/env python3

from LinkedList import Element, LinkedList


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    assert (stack.pop().value == 3)
    assert (stack.pop().value == 2)
    assert (stack.pop().value == 1)
    assert (stack.pop() is None)
    stack.push(e4)
    assert (stack.pop().value == 4)

    print("Passed")
