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




def index_files(path: str, index: AbstractIndex) -> None:
    # path should contain the location of the news articles you want to parse
    if path is not None:
        print(f"path = {path}")

    # a sample json news article.  assume this is in a file named sample.json
    sample_filename = "test2.json"
    sample_json = """
    {
        "organizations": [],
        "uuid": "e49cf1a0134f50860eb70214b4416f2cc0715d30",
        "author": "",
        "url": "https://www.reuters.com/article/brief-roku-says-youtube-tv-now-available/brief-roku-says-youtube-tv-now-available-on-roku-devices-idUSFWN1PR0WL",
        "ord_in_thread": 0,
        "title": "BRIEF-Roku Says Youtube TV Now Available On Roku Devices",
        "locations": [],
        "highlightText": "",
        "language": "english",
        "persons": [],
        "text": "Feb 1 (Reuters) - Roku Inc:\n* ROKU INC SAYS YOUTUBE TV NOW AVAILABLE ON ROKU DEVICES Source text for Eikon: Further company coverage:\n ",
        "published": "2018-02-01T16:16:00.000+02:00",
        "crawled": "2018-02-01T16:30:53.000+02:00",
        "highlightTitle": "",
        "preprocessed_text": [
            "feb",
            "reute
            "roku",
            "inc",
            "roku",
            "inc",
            "say",
            "youtube",
            "tv",
            "available",
            "roku",
            "device",
            "source",
            "text",
            "eikon",
            "company",
            "coverage"
     ]
    }
    """

    # extract the preprocessed_text words and add them to the index with
    # sample.json as the file name
    the_json = json.loads(sample_json)
    words = the_json["preprocessed_text"]

    for word in words:
        index.insert(word, sample_filename)


# A simple demo of how the @timer decoration can be used
@timer
def loopy_loop():
    total = sum((x for x in range(0, 1000000)))


def main():
    # You'll need to change this to be the absolute path to the root folder
    # of the dataset
    data_directory = "/Users/mihaliskoutouvos/Downloads/final_pickles/hash_index.pkl"

    # Here, we are creating a sample binary search tree index object
    # and sending it to the index_files function
    hm_index = HashMapIndex()
    index_files(data_directory, hm_index)

    # As a gut check, we are printing the keys that were added to the
    # index in order.
    print(hm_index.get_keys_in_order())

    # quick demo of how to use the timing decorator included
    # in indexer.util
    loopy_loop()


if __name__ == "__main__":
    main()
