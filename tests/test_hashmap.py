import unittest
from indexer.maps.hash_map import HashMapIndex

class TestHashMapIndex(unittest.TestCase):
    def setUp(self):
        self.index = HashMapIndex()

    def test_add_and_search(self):
        self.index.add("apple", 1)
        self.index.add("banana", 2)
        self.index.add("apple", 3)
        
        self.assertEqual(self.index.search("apple"), {1, 3})
        self.assertEqual(self.index.search("banana"), {2})
        self.assertEqual(self.index.search("cherry"), set())
    
    def test_remove(self):
        self.index.add("dog", 5)
        self.index.add("cat", 6)
        self.assertEqual(self.index.search("dog"), {5})
        
        self.index.remove("dog")
        self.assertEqual(self.index.search("dog"), set())
    
    def test_get_keys_in_order(self):
        self.index.add("x", 10)
        self.index.add("y", 20)
        self.index.add("z", 30)
        
        self.assertEqual(self.index.get_keys_in_order(), ["x", "y", "z"])
        
        self.index.remove("y")
        self.assertEqual(self.index.get_keys_in_order(), ["x", "z"])
    
    def test_insert_alias(self):
        self.index.insert("alpha", 100)
        self.assertEqual(self.index.search("alpha"), {100})
    
    def test_iteration(self):
        self.index.add("red", 50)
        self.index.add("blue", 60)
        self.assertEqual(list(iter(self.index)), ["red", "blue"])

if __name__ == "__main__":
    unittest.main()
