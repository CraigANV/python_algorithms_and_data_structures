#!/usr/bin/env python3

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


if __name__ == "__main__":
    print("Running {} tests".format(__file__))

    # Test Cases
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    assert (q.peek() == 1)

    # Test dequeue
    assert (q.dequeue() == 1)

    # Test enqueue
    q.enqueue(4)
    assert (q.dequeue() == 2)
    assert (q.dequeue() == 3)
    assert (q.dequeue() == 4)

    q.enqueue(5)
    assert (q.peek() == 5)
