from indexer.abstract_index import AbstractIndex
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.lists.list_index import ListIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
import random
import string
import pickle

# Generate random strings
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


bst_index = BinarySearchTreeIndex()
avl_index = AVLTreeIndex()
hm_index = HashMapIndex()
l_index = ListIndex()


# E1: Search time for existing elements
@timer
def experiment_search_existing(index, n):
    search_times = []
    for i in range(n):
        term = f"term{i}"
        values = index.search(term)
        search_times.append(values)
    return search_times


# Insert 100 keys first (so they exist before searching)
for i in range(100):
    bst_index.insert(f"term{i}", f"value{i}")
    avl_index.insert(f"term{i}", f"value{i}")
    hm_index.insert(f"term{i}", f"value{i}")
    l_index.insert(f"term{i}", f"value{i}")

# Now perform search experiments
print("E1 Experiments")
experiment_search_existing(bst_index, 100)
experiment_search_existing(avl_index, 100)
experiment_search_existing(hm_index, 100)
experiment_search_existing(l_index, 100)

# E2: Search time for non-existing elements
@timer
def experiment_search_non_existing(index, n):
    search_times = []
    for i in range(n):
        term = f"non_existing_term{i}"
        try: 
            search_time = index.search(term)
            search_times.append(search_time)
        except KeyError: 
            pass
    return search_times

# Now perform search experiments
print("E2 Experiments")
experiment_search_non_existing(bst_index, 100)
experiment_search_non_existing(avl_index, 100)
experiment_search_non_existing(hm_index, 100)
experiment_search_non_existing(l_index, 100)


#E3: Check Inserting Time
@timer 
def insert_items(index, n):
    for i in range(n):
        key = generate_random_string(12)
        value = generate_random_string(12)
        index.insert(key, value)


# Now perform search experiments
print("E3 Experiments")
insert_items(bst_index, 100)
insert_items(avl_index, 100)
insert_items(hm_index, 100)
insert_items(l_index, 100)
