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

    parser = argparse.ArgumentParser(description='Index news articles and save to a pickle file.')
    parser.add_argument('-d', '--dataset', required=True, help='Path to the root folder of the dataset.')
    parser.add_argument('-p', '--pickle', required=True, help='Path to the pickle file.')
    args = parser.parse_args()

    avl_tree = AVLTreeIndex()
    list_index = ListIndex()
    hash_map = HashMapIndex()
    bst_index = BinarySearchTreeIndex()

    folder_path = args.dataset
    save_path = args.pickle

    # Option to load existing index
    if os.path.exists(save_path):
        hash_map = load_index(save_path)
    else:
        index_files(hash_map, folder_path, save_path)

    # Print the contents of the hash_map to verify
    print("HashMap Index Contents:")
    for term, document_ids in hash_map.hash_map.items():
        print(f"Term: {term}, Document IDs: {document_ids}")  
              
if __name__ == '__main__':
    main()
