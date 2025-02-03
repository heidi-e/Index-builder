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

bst_index = BinarySearchTreeIndex()
avl_index = AVLTreeIndex()
hm_index = HashMapIndex()
l_index = ListIndex()


# Generate random strings
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# E1: Search time for existing elements
@timer
def experiment_search_existing(index, n):
    """
        Searching for existing values

        Args:
            index - one of the four data structres
            n - amount of values to check

        Results:
            Nothing, but prints out counts for tokens and articles 
        """
    
    #Initializing values
    articles_passed = set()
    tokens = 0
    search_times = []
    
    #Appending terms to our variables holding info
    for i in range(n):
        term = f"term{i}"
        try: 
            values = index.search(term)
            tokens = tokens + 1
            articles_passed.update(values)
            search_times.append(values)
        except KeyError: 
            pass
    
    articles_indexed_during_exp = len(articles_passed)
    tokens_identified = tokens

    print(articles_indexed_during_exp, tokens_identified)



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
    """
        Searching for non-existing values

        Args:
            index - one of the four data structres
            n - amount of values to check

        Results:
            Nothing, but prints out counts for tokens and articles 
        """
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





def index_files(path: str, index: AbstractIndex) -> None:
    """
        Indexing the search data sets

        Args:
            path - file path as a string
            index - one of the four data structures

        Results:
            Nothing, but prints out counts for tokens and articles 
        """
    #Initializing values
    token_count = 0
    article_count = 0

    # path should contain the location of the news articles you want to parse
    if path is not None:
        print(f"path = {path}")

    #Load json file
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    #Checking if dataset does not appear as a valid entry in the search datasets
    for val in data:
        if 'dataset' not in val or not isinstance(val['dataset'], list):
            continue

        dataset = val['dataset']
        
        for token in data:
            index.insert(token, "dataset")
            token_count = token_count + 1
        article_count = article_count + len(dataset)

    #Printing totals for tokens and articles passed
    print(token_count, article_count)


# A simple demo of how the @timer decoration can be used
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))


def load_pickle_files(index, pickled_data, data_file):
    """
        Opens and loads the pickled files for indexing purposes

        Args:
            index - one of the four data structurs
            pickled_data - the pickled file
            data_file - the search datasets 

        Results:
            The data structure used
        """
    if os.path.exists(pickled_data):
        with open(pickled_data, 'rb') as file:
            index = pickle.load(file)
    else: 
        index_files(data_file, index)
        with open(pickled_data, 'wb') as file:
            pickle.dump(index, file)
    
        return index


def main():
    """
        Update the height of a node

        Args:
            None

        Results:
            Values including the time it took, in nanoseconds, for the experiments to run for each data structure
        """
    #Objects for the data structures
    bst_index = BinarySearchTreeIndex()
    avl_index = AVLTreeIndex()
    hm_index = HashMapIndex()
    l_index = ListIndex()

    #Pickled data files
    pickle_data_bst = '/Users/mihaliskoutouvos/Downloads/final_pickles 2/bst_index.pkl'
    pickle_data_avl = '/Users/mihaliskoutouvos/Downloads/final_pickles 2/avl_index.pkl'
    pickle_data_ht =  '/Users/mihaliskoutouvos/Downloads/final_pickles 2/hash_index.pkl'
    pickle_data_l = '/Users/mihaliskoutouvos/Downloads/final_pickles 2/list_index.pkl'
    data_directory = '/Users/mihaliskoutouvos/Downloads/compiled_datasets.json'

    
    load_pickle_files(bst_index, pickle_data_bst, data_directory)
    load_pickle_files(avl_index, pickle_data_avl, data_directory)
    load_pickle_files(hm_index, pickle_data_ht, data_directory)
    load_pickle_files(l_index, pickle_data_l, data_directory)
    
    # As a gut check, we are printing the keys that were added to the
    # index in order.
    print(bst_index.get_keys_in_order())
    print(avl_index.get_keys_in_order())
    print(hm_index.get_keys_in_order())
    print(l_index.get_keys_in_order())
    

    #Indexing the datasets using a specific data structure
    index_files(data_directory, bst_index)
    index_files(data_directory, avl_index)
    index_files(data_directory, hm_index)
    index_files(data_directory, l_index)

    # Fontenot's loop function, not too useful for us here. 
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

if __name__ == "__main__":
    main()