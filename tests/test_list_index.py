"""
This module contains unit tests for the ListIndex class.

The ListIndex class is responsible for implementing a list index for a search engine.
The following tests are included:
- `test_insert_and_search`: Tests the `insert` and `search` methods of the ListIndex class.
- `test_insert_duplicate_keys`: Tests the behavior of inserting duplicate keys into the ListIndex class.
- `test_search_non_existent_key`: Tests the behavior of searching for a non-existent key in the ListIndex class.
- `test_get_keys_in_order`: Tests the `get_keys_in_order` method of the ListIndex class.
"""

import pytest
from indexer.lists.list_index import ListIndex


@pytest.fixture
def lst():
    return ListIndex()


def test_insert_and_search(lst):
    lst.insert('a', 1)
    lst.insert('b', 2)
    lst.insert('c', 3)

    assert lst.search('a') == [1]
    assert lst.search('b') == [2]
    assert lst.search('c') == [3]


def test_insert_duplicate_keys(lst):
    lst.insert('a', 1)
    lst.insert('a', 2)
    lst.insert('a', 3)

    assert lst.search('a') == [1, 2, 3]


def test_search_non_existent_key(lst):
    lst.insert('a', 1)

    with pytest.raises(KeyError):
        lst.search('b')


def test_get_keys_in_order(lst):
    lst.insert('b', 2)
    lst.insert('a', 1)
    lst.insert('c', 3)

    assert lst.get_keys_in_order() == ['a', 'b', 'c']

if __name__ == "__main__":
    pytest.main()