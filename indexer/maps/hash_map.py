from indexer.abstract_index import AbstractIndex


class HashMapIndex(AbstractIndex):
    '''
    A HashMap-based implementation of an index that maps a key (term) to a set of document IDs.

    The HashMapIndex class uses an internal dictionary (`hash_map`) to store terms as keys and 
    their associated document IDs as sets of values. It provides methods to add, search, 
    remove terms, and iterate over the terms stored in the index. It also includes an alias 
    for the `add` method called `insert` for compatibility with other indexing systems. 
    '''

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
        Alias for add method (test function needed it)
        """
        self.add(term, document_id)

    def get_keys_in_order(self):
        # Return a list of all keys
        return list(self.hash_map.keys())