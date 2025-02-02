from indexer.abstract_index import AbstractIndex

class HashMapIndex(AbstractIndex):
    class Node:
        """A node in the linked list for separate chaining"""
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=100):
        super().__init__()
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity
        self.key_order = []

    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, term, document_id):
        existing = self._get(term)
        if existing is None:
            existing = set()
            if term not in self.key_order:
                self.key_order.append(term)
        existing.add(document_id)
        self._put(term, existing)

    def search(self, term):
        return self._get(term) or set()

    def remove(self, term):
        self._remove(term)
        if term in self.key_order:
            self.key_order.remove(term)

    def insert(self, term, document_id):
        self.add(term, document_id)

    def get_keys_in_order(self):
        return self.key_order

    def _put(self, key, value):
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = self.Node(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = self.Node(key, value)
        self.size += 1

    def _get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def _remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def __iter__(self):
        return iter(self.key_order)
