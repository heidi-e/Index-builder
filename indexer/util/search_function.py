import json
from urllib.parse import urlparse
import re
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.lists.list_index import ListIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
import os
import pickle
from indexer.util.timer import timer
import argparse
import time
from indexer.util.parser_utils import preprocess_text


def extract_article_data(file_path):
    """
    Extract the metadata (title, domain, author) & preprocessed text from a JSON file containing an article
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        article = json.load(f)

    title = article.get('title', '')
    source_url = article.get('url', '')
    author = article.get('author', '')

    # Take the domain from the source URL (www.google/words/morewords.com changed to www.google.com)
    domain = urlparse(source_url).netloc

    # Converts preprocessed text
    preprocessed_text = ' '.join(article.get('preprocessed_text', []))

    return title, domain, author, preprocessed_text


def process_article(index_structure, file_path, filename):
    """
    Process an article & store words in the indexing structure
    """
    title, domain, author, preprocessed_text = extract_article_data(file_path)

    # clean up title
    title = preprocess_text(f"{title}")

    # Combines text for indexing
    text_to_index = f"{title} {domain} {author} {preprocessed_text}"

    # Tokenize text (split by whitespace & remove any punctuation)
    words = re.findall(r'\b\w+\b', text_to_index.lower())


    # Add words to the index with the filename
    for word in words:
        index_structure.insert(word, filename)

@timer
def index_files(index, folder_path, save_path):
    """
    Crawl through folders of news articles and index them.
    """
    print("Starting crawl and index...")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                process_article(index, file_path, file)
            
    save_index(index, save_path)


def save_index(index, file_path):
    """
    Save the index to a pickle file.
    """
    with open(file_path, 'wb') as f:
        pickle.dump(index, f)
    print(f"Index saved to {file_path}")


def load_index(file_path):
    """
    Load the index from a pickle file.
    """
    with open(file_path, 'rb') as f:
        index = pickle.load(f)
    print(f"Index loaded from {file_path}")
    return index

def specify_dataset(index):
    """
    To confirm searching produces correct results

    """
    search_words = ['northeastern', 'beanpot', 'husky']
    # search for articles with specific words
    for word in search_words:
        result = index.search(word)
        print(result)


def main():


    # use command line to input specific directories for dataset input and output
    parser = argparse.ArgumentParser(description="Indexing program for news articles.")
    # Dataset path argument (required)
    parser.add_argument("-d", "--dataset", required=True, help="Path to the dataset root folder.")
    # Set path to save pickled index
    parser.add_argument("-p", "--pickle", required=True, help="Path to save or load the index using pickle.")

    args = parser.parse_args()

    # set desired indexing structure
    #avl_tree = AVLTreeIndex()
    #list_index = ListIndex()
    #hash_map = HashMapIndex()
    bst_index = BinarySearchTreeIndex()

    start_time = time.time()

    # extract, parse, index metadata into pickled index
    index_files(bst_index, args.dataset, args.pickle)

    end_time = time.time()
    print(f"Total indexing time: {end_time - start_time:.2f} seconds")

    specify_dataset(bst_index)

    # test by loading and printing pickled data
    #index = load_index(args.pickle)
    #keys = index.get_keys_in_order()[:5]
    #print(keys)

if __name__ == '__main__':
    main()
