import json
from urllib.parse import urlparse
import re
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.lists.list_index import ListIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
import os


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


def crawl_and_index(index, folder_path):
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

def main():


    # Usage Example
    avl_tree = AVLTreeIndex()
    list = ListIndex()
    hash_map = HashMapIndex()

    file_path = 'indexer/util/test.json'
    file_name = 'test.json'
    folder_path = 'indexer/util'

    # process_article(avl_tree, file_path)
    # process_article(list, file_path)
    # process_article(hash_map, file_path, file_name) 
    crawl_and_index(hash_map, folder_path)

    # Print the contents of the hash_map to verify
    print("HashMap Index Contents:")
    for term, document_ids in hash_map.hash_map.items():
        print(f"Term: {term}, Document IDs: {document_ids}")
              
if __name__ == '__main__':
    main()





# def crawl_data(index_struct, file_path):
#     """
#     Crawl folders of news articles and extract metadata
#     Args:
#         index_struct: index structure you are testing
#         file_path: path to the folder containing the dataset

#     Returns:

#     """

#     # Load the JSON file
#     with open(file_path, "r") as f:
#         data = json.load(f)

#     for file in data:

#         # Extract relevant fields
#         title = file["title"]
#         url = file['url']
#         if file['author'] != "":
#             author = file['author'].split('')[1]

#         # Extract preprocessed text
#         raw_preprocessed_text = file["preprocessed_text"]

#         # store into indexing structure
#         for word in raw_preprocessed_text:
#             index_struct.insert(word, file)
#             index_struct.insert(word, title)
#             index_struct.insert(word, url)
#             index_struct.insert(word, author)


