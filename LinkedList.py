#!/usr/bin/env python3


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """ Appends a new element to the List"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """ Returns the element at a certain position"""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """ Add an element to a particular spot in the list"""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted


if __name__ == "__main__":
    print("Running {} tests".format(__file__))

    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    assert (ll.head.next.next.value == 3)
    assert (ll.get_position(3).value == 3)

    # Test insert
    ll.insert(e4, 3)

    assert (ll.get_position(3).value == 4)

    # Test delete
    ll.delete(1)

    assert (ll.get_position(1).value == 2)
    assert (ll.get_position(2).value == 4)
    assert (ll.get_position(3).value == 3)

    # Test insert_first
    ll.insert_first(e1)
    assert (ll.get_position(1).value == 1)

    # Test delete_first
    assert (ll.delete_first().value == 1)
    assert (ll.get_position(1).value == 2)
