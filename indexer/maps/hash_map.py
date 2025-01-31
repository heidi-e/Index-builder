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
        Alias for add method (test function needed it)
        """ 
        self.add(term, document_id)


    def get_keys_in_order(self):
        # Return a list of all keys 
        return list(self.hash_map.keys())