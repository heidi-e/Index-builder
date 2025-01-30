from indexer.maps.AVL import HashMapIndex 

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