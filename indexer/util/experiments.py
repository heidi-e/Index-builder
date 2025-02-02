from indexer.abstract_index import AbstractIndex
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.lists.list_index import ListIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
import random
import string
import json
import pickle
import os 


# Generate random strings
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



# E1: Search time for existing elements
@timer
def experiment_search_existing(index, id, n, docs_searched, tokens_counted):
    
    articles_passed = set()
    tokens = 0
    search_times = []
    
    for i in range(n):
        term = f"term{i}"
        try: 
            values = index.search(term)
            tokens = tokens + 1
            articles_passed.update(values)
            search_times.append(values)
        except KeyError: 
            pass
    
    docs_indexed_during_exp = len(docs_searched)
    tokens_identified = tokens_counted

    print(docs_indexed_during_exp, tokens_identified)



# Insert 100 keys first (so they exist before searching)
for i in range(100):
    bst_index.insert(f"term{i}", f"value{i}")
    avl_index.insert(f"term{i}", f"value{i}")
    hm_index.insert(f"term{i}", f"value{i}")
    l_index.insert(f"term{i}", f"value{i}")

#

# E2: Search time for non-existing elements
@timer
def experiment_search_non_existing(index, n):
    articles_passed = set()
    tokens = 0
    search_times = []

    for i in range(n):
        term = f"non_existing_term{i}"
        try: 
            search_time = index.search(term)
            search_times.append(search_time)
        except KeyError: 
            pass

    print(articles_passed, tokens)

#


#E3: Check Inserting Time
@timer 
def insert_items(index, n):
    for i in range(n):
        key = generate_random_string(12)
        value = generate_random_string(12)
        index.insert(key, value)

    print(index, n)




def index_files(path: str, index: AbstractIndex) -> None:
    token_count = 0
    article_count = 0

    # path should contain the location of the news articles you want to parse
    if path is not None:
        print(f"path = {path}")

    
    with open(path, 'r', encode='utf-8') as file:
        data = json.load(file)

    for token in data.get('dataset', None):
        article_count = article_count + 1
        token_count = len(token)

        for word in token:
            index.insert(word, "dataset")

    print(token_count, article_count)


# A simple demo of how the @timer decoration can be used
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))


def main():

    pickle_data_bst = '/Users/mihaliskoutouvos/Downloads/final_pickles 2/bst_index.pkl'
    pickle_data_avl = '/Users/mihaliskoutouvos/Downloads/final_pickles 2/avl_index.pkl'
    pickle_data_ht =  '/Users/mihaliskoutouvos/Downloads/final_pickles 2/hash_index.pkl'
    pickle_data_l = '/Users/mihaliskoutouvos/Downloads/final_pickles 2/list_index.pkl'
    data_directory = '/Users/mihaliskoutouvos/Downloads/compiled_datasets.json'
    

    bst_index = BinarySearchTreeIndex()
    avl_index = AVLTreeIndex()
    hm_index = HashMapIndex()
    l_index = ListIndex()

    index_files(data_directory, bst_index)
    index_files(data_directory, avl_index)
    index_files(data_directory, hm_index)
    index_files(data_directory, l_index)

    # As a gut check, we are printing the keys that were added to the
    # index in order.
    print(bst_index.get_keys_in_order())
    print(avl_index.get_keys_in_order())
    print(hm_index.get_keys_in_order())
    print(l_index.get_keys_in_order())

    # quick demo of how to use the timing decorator included
    # in indexer.util
    loopy_loop()

    # Now perform search experiments
    print("E1 Experiments")
    experiment_search_existing(bst_index, 100)
    experiment_search_existing(avl_index, 100)
    experiment_search_existing(hm_index, 100)
    experiment_search_existing(l_index, 100)

    # Now perform search experiments
    print("E2 Experiments")
    experiment_search_non_existing(bst_index, 100)
    experiment_search_non_existing(avl_index, 100)
    experiment_search_non_existing(hm_index, 100)
    experiment_search_non_existing(l_index, 100)

    # Now perform search experiments
    print("E3 Experiments")
    insert_items(bst_index, 100)
    insert_items(avl_index, 100)
    insert_items(hm_index, 100)
    insert_items(l_index, 100)


if __name__ == "__main__":
    main()