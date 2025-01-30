from indexer.abstract_index import AbstractIndex

class HashMapIndex(AbstractIndex):
    
    def __init__(self):
        super().__init__()
        self.hash_map = {}

    def add(self, term, document_id):
        """
        Add a document ID to the set of document IDs associated with a term
        """ 
        if term not in self.hash_map:
            self.hash_map[term] = set()
        self.hash_map[term].add(document_id)

    def search(self, term):
        """
        Search for the set of document IDs associated with a term
        """ 
        return self.hash_map.get(term, set())

    def remove(self, term):
        """
        Remove a term and its associated document IDs from the hashmap
        """ 
        if term in self.hash_map:
            del self.hash_map[term]

    def __iter__(self):
        """
        Return an iterator over the terms in the hashmap
        """ 
        return iter(self.hash_map)

    def insert(self, term, document_id):
        """
        Alias for add method
        """ 
        self.add(term, document_id)


def test_hash_map_index():
    index = HashMapIndex()
    
    # Test adding terms and document IDs
    index.add("apple", 1)
    index.add("banana", 2)
    index.add("apple", 3)

    assert index.search("apple") == {1, 3}, "Test case for adding/searching 'apple' failed"
    assert index.search("banana") == {2}, "Test case for adding/searching 'banana' failed"
    assert index.search("cherry") == set(), "Test case for searching non-existent term 'cherry' failed"
    
    # Test removing terms
    index.remove("apple")
    assert index.search("apple") == set(), "Test case for removing 'apple' failed"
    
    index.remove("banana")
    assert index.search("banana") == set(), "Test case for removing 'banana' failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_hash_map_index()