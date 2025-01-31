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
    title, domain, author, preprocessed_text  = extract_article_data(file_path)
    
    # Combines text for indexing
    text_to_index = f"{title} {domain} {author} {preprocessed_text}"
    
    # Tokenize text (split by whitespace & remove any punctuation)
    words = re.findall(r'\b\w+\b', text_to_index.lower())

    # Add words to the index with the filename
    for word in words:
        index_structure.insert(word, filename)


def crawl_and_index(index, folder_path, save_path):
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

@timer
def search_hash_map(index, word):
    return index.search(word)

@timer
def search_avl_tree(index, word):
    return index.search(word)

@timer
def search_list(index, word):
    return index.search(word)

@timer
def search_bst(index, word):
    return index.search(word)



def main():

    # Usage Example
    avl_tree = AVLTreeIndex()
    list_index = ListIndex()
    hash_map = HashMapIndex()
    bst_index = BinarySearchTreeIndex()

    file_path = 'indexer/util/test.json'
    file_name = 'test.json'
    folder_path = 'indexer/util'

    crawl_and_index(hash_map, folder_path)

    word = "hello"
    
    # search_hash_map(hash_map, word)
    # search_avl_tree(avl_tree, word)
    # search_list(list_index, word)
    # search_bst(bst_index, word)
              
if __name__ == '__main__':
    main()
