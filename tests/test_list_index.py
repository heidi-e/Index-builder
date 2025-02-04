"""
This module contains unit tests for the ListIndex class.

The ListIndex class is responsible for implementing a list-based index for a search engine.
The following tests are included:
- `test_insert_and_search`: Tests the `insert` and `search` methods of the ListIndex class.
- `test_get_keys_in_order`: Tests the `get_keys_in_order` method of the ListIndex class.
- `test_count_keys`: Tests the `count_keys` method of the ListIndex class.
- `test_get_avg_value_list_len`: Tests the `get_avg_value_list_len` method of the ListIndex class.
- `test_iterate`: Tests the iteration functionality of the ListIndex class.
"""

import pytest
from indexer.lists.list_index import ListIndex  


@pytest.fixture
def list_index():
    return ListIndex()


def test_insert_and_search(list_index):
    list_index.insert('term1', 'value1')
    list_index.insert('term1', 'value2')
    list_index.insert('term2', 'value3')

    # Test search
    assert list_index.search('term1') == ['value1', 'value2']
    assert list_index.search('term2') == ['value3']
    assert list_index.search('term3') == []


def test_get_keys_in_order(list_index):
    list_index.insert('term3', 'value1')
    list_index.insert('term1', 'value2')
    list_index.insert('term2', 'value3')

    keys = list_index.get_keys_in_order()
    assert keys == ['term1', 'term2', 'term3']


def test_count_keys(list_index):
    list_index.insert('term1', 'value1')
    list_index.insert('term2', 'value2')
    list_index.insert('term3', 'value3')

    # Test counting unique keys
    assert list_index.count_keys() == 3

    list_index.insert('term1', 'value4')
    assert list_index.count_keys() == 3  # Duplicate keys should not increase count


def test_get_avg_value_list_len(list_index):
    list_index.insert('term1', 'value1')
    list_index.insert('term1', 'value2')
    list_index.insert('term2', 'value3')

    # Test average number of values per key
    assert list_index.get_avg_value_list_len() == 1.5

    # Test when the index is empty
    empty_list_index = ListIndex()
    assert empty_list_index.get_avg_value_list_len() == 0.0


def test_iterate(list_index):
    list_index.insert('term1', 'value1')
    list_index.insert('term2', 'value2')

    # Test iteration over the list index
    terms = [entry[0] for entry in list_index]
    assert 'term1' in terms
    assert 'term2' in terms

if __name__ == "__main__":
  pytest.main()
