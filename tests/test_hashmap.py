"""
This module contains unit tests for the HashMapIndex class.

The HashMapIndex class is responsible for implementing a hashmap-based index for a search engine.
The following tests are included:
- `test_add_and_search`: Tests the `add` and `search` methods of the HashMapIndex class.
- `test_remove`: Tests the `remove` method of the HashMapIndex class.
- `test_iterate`: Tests the iteration functionality of the HashMapIndex class.
- `test_get_keys_in_order`: Tests the `get_keys_in_order` method of the HashMapIndex class.
- `test_insert_alias`: Tests the `insert` method, ensuring it works as an alias for the `add` method.
"""

import pytest
from indexer.abstract_index import AbstractIndex
from indexer.maps.hash_map import HashMapIndex  


@pytest.fixture
def hashmap_index():
    return HashMapIndex()


def test_add_and_search(hashmap_index):
    hashmap_index.add('term1', 1)
    hashmap_index.add('term1', 2)
    hashmap_index.add('term2', 3)

    # Test search
    assert hashmap_index.search('term1') == {1, 2}
    assert hashmap_index.search('term2') == {3}
    assert hashmap_index.search('term3') == set()


def test_remove(hashmap_index):
    hashmap_index.add('term1', 1)
    hashmap_index.add('term1', 2)
    
    # Test removing a term
    hashmap_index.remove('term1')
    assert hashmap_index.search('term1') == set()
    
    # Ensure removing a non-existent term doesn't cause issues
    hashmap_index.remove('term3')
    assert hashmap_index.search('term3') == set()


def test_iterate(hashmap_index):
    hashmap_index.add('term1', 1)
    hashmap_index.add('term2', 2)
    hashmap_index.add('term3', 3)

    terms = set(hashmap_index)
    assert 'term1' in terms
    assert 'term2' in terms
    assert 'term3' in terms


def test_get_keys_in_order(hashmap_index):
    hashmap_index.add('term1', 1)
    hashmap_index.add('term3', 3)
    hashmap_index.add('term2', 2)

    keys = hashmap_index.get_keys_in_order()
    assert keys == ['term1', 'term3', 'term2']


def test_insert_alias(hashmap_index):
    hashmap_index.insert('term1', 1)
    hashmap_index.insert('term1', 2)

    # Test that the insert method is an alias for add
    assert hashmap_index.search('term1') == {1, 2}

if __name__ == "__main__":
  pytest.main()
