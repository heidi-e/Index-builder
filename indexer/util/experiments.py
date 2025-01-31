from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.lists.list_index import ListIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
import random
import string

# Generate random strings
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# E1: Search time for existing elements
@timer
def experiment_search_existing(index, n):
    search_times = []
    for i in range(n):
        term = f"term{i}"
        _, search_time = index.search(term)
        search_times.append(search_time)
    return search_times

# E2: Search time for existing elements
@timer
def experiment_search_non_existing(index, n):
    search_times = []
    for i in range(n):
        term = f"non_existing_term{i}"
        _, search_time = index.search(term)
        search_times.append(search_time)
    return search_times



