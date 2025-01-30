"""
This module contains unit tests for the ListIndex class.

The ListIndex class is responsible for implementing a listing index for a search engine.
The following tests are included:
- `test_insert_and_search`: Tests the `insert` and `search` methods of the ListIndex class.
- `test_insert_duplicate_keys`: Tests the behavior of inserting duplicate keys into the BinarySearchTreeIndex class.
- `test_search_non_existent_key`: Tests the behavior of searching for a non-existent key in the BinarySearchTreeIndex class.
- `test_count_nodes`: Tests the `count_nodes` method of the BinarySearchTreeIndex class.
- `test_tree_height`: Tests the `tree_height` method of the BinarySearchTreeIndex class.
- `test_get_keys_in_order`: Tests the `get_keys_in_order` method of the BinarySearchTreeIndex class.
- `test_get_leaf_keys`: Tests the `get_leaf_keys` method of the BinarySearchTreeIndex class.
"""

import pytest
from indexer.lists.list_index import ListIndex

def test_list_index():
    index = ListIndex()

    # Test adding terms and document IDs
    index.insert("apple", 1)
    index.insert("banana", 2)
    index.insert("apple", 3)

    assert index.search("apple") == [1, 3], "Test case for adding/searching 'apple' failed"
    assert index.search("banana") == [2], "Test case for adding/searching 'banana' failed"
    assert index.search("cherry") == [], "Test case for searching non-existent term 'cherry' failed"


    print("All test cases passed!")

if __name__ == "__main__":
    test_list_index()
