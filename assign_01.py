import json
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.trees.bst_index import HashMapIndex
from indexer.trees.bst_index import ListIndex
from indexer.util.timer import timer
from indexer.abstract_index import AbstractIndex


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
        "reuters",
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
