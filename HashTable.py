#!/usr/bin/env python3


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        hv = (ord(string[0]) * 100) + ord(string[1])
        return hv


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    # Setup
    hash_table = HashTable()

    # Test calculate_hash_value
    assert (hash_table.calculate_hash_value('UDACITY') == 8568)

    # Test lookup edge case
    assert (hash_table.lookup('UDACITY') == -1)

    # Test store
    hash_table.store('UDACITY')
    assert (hash_table.lookup('UDACITY') == 8568)

    # Test store edge case
    hash_table.store('UDACIOUS')
    assert (hash_table.lookup('UDACIOUS') == 8568)
