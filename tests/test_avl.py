"""
This module contains unit tests for the AVLTreeIndex class.

The AVLTreeIndex class is responsible for implementing a binary search tree index for a search engine.
The following tests are included:
- `test_insert_and_search`: Tests the `insert` and `search` methods of the AVLTreeIndex class.
- `test_insert_duplicate_keys`: Tests the behavior of inserting duplicate keys into the AVLIndex class.
- `test_search_non_existent_key`: Tests the behavior of searching for a non-existent key in the AVLTreeIndex class.
- `test_count_nodes`: Tests the `count_nodes` method of the AVLTreeIndex class.
- `test_tree_height`: Tests the `tree_height` method of the AVLTreeIndex class.
- `test_get_keys_in_order`: Tests the `get_keys_in_order` method of the AVLTreeIndex class.
- `test_get_leaf_keys`: Tests the `get_leaf_keys` method of the AVLTreeIndex class.
"""

import pytest
from indexer.trees.avl_index import AVLTreeIndex
from indexer.trees.avl_node import AVLNode


@pytest.fixture
def avl():
    return AVLTreeIndex()


def test_insert_and_search(avl):
    avl.insert('a', 1)
    avl.insert('b', 2)
    avl.insert('c', 3)

    assert avl.search('a') == [1]
    assert avl.search('b') == [2]
    assert avl.search('c') == [3]


def test_insert_duplicate_keys(avl):
    avl.insert('a', 1)
    avl.insert('a', 2)
    avl.insert('a', 3)

    assert avl.search('a') == [1, 2, 3]


def test_search_non_existent_key(avl):
    avl.insert('a', 1)

    with pytest.raises(KeyError):
        avl.search('b')


def test_count_nodes(avl):
    avl.insert('a', 1)
    avl.insert('b', 2)
    avl.insert('c', 3)

    assert avl.count_nodes() == 3


def test_tree_height(avl):
    avl.insert('a', 1)
    avl.insert('b', 2)
    avl.insert('c', 3)

    assert avl.tree_height() == 3


def test_get_keys_in_order(avl):
    avl.insert('b', 2)
    avl.insert('a', 1)
    avl.insert('c', 3)

    assert avl.get_keys_in_order() == ['a', 'b', 'c']


def test_get_leaf_keys(avl):
    avl.insert('b', 2)
    avl.insert('a', 1)
    avl.insert('c', 3)

    assert avl.get_leaf_keys() == ['a', 'c']


if __name__ == "__main__":
    pytest.main()