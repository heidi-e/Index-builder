from indexer.abstract_index import AbstractIndex
from indexer.maps.hash_map import HashMapIndex
from indexer.trees.avl_tree import AVLTreeIndex
from indexer.lists.list_index import ListIndex
from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.util.timer import timer
import json
import pickle
import time
import pandas as pd
from typing import List
from openpyxl import load_workbook

bst_index = BinarySearchTreeIndex()
avl_index = AVLTreeIndex()
hm_index = HashMapIndex()
l_index = ListIndex()


# E1: Search time for existing elements

def experiment_searching(index_name, index, datasets, n_list, run_id, compute_proc_type, primary_memory_size):


    df = pd.DataFrame()

    # initialize counters for each dataset
    total_docs_indexed = 0
    total_tokens_indexed = 0

    for i in range(len(datasets)):  
        docs_indexed = 0      # Total num of documents indexed for this dataset
        tokens_indexed = 0    # Total num of tokens indexed for this dataset

        start_time = time.time() 

        # iterate through each word in list of words
        for word in datasets[i]:   
            try:
                # run search function
                list_of_articles = index.search(word)  

                # If articles are found for the word, add to the respective counters
                if list_of_articles:
                    docs_indexed += len(list_of_articles) 
                    tokens_indexed += 1

            except KeyError:
                # If the word isn't found in the index, continue with the next word
                pass

        # Accumulate totals for all datasets
        total_docs_indexed += docs_indexed
        total_tokens_indexed += tokens_indexed

        end_time = time.time()  
        search_time = end_time - start_time
        search_time_ns = int(search_time * 1e9)

        # Final dictionary for overall counts
        overall_summary = {
            'run_id': run_id,
            'compute_proc_type': compute_proc_type,
            'primary_memory_size': primary_memory_size,
            'index_type': index_name,
            'dataset': i+1,
            'num_docs_indexed': total_docs_indexed,
            'num_tokens_indexed': total_tokens_indexed,
            'search_set_base_size': n_list[i],
            'search_time': search_time_ns
        }

        # Convert data to a DataFrame (one row)
        new_row = pd.DataFrame([overall_summary])

        # Append the new row to the DataFrame
        df = pd.concat([df, new_row], ignore_index=True)

    return df


# E2: Search time for non-existing elements
def experiment_missing_words(index_name, index, datasets, n_list, run_id, compute_proc_type, primary_memory_size):
    """
    Identifies the number of words in datasets that are not found in the given index and records the time taken.
    """
    df = pd.DataFrame()
    
    for i, dataset in enumerate(datasets):  
        unindexed_word_count = 0  # Counter for words not found
        docs_indexed = 0
        start_time = time.time() 
        
        for word in dataset:
            try:
                # search for word in index
                list_of_articles = index.search(word)
                # count number of docs indexed
                if list_of_articles:
                    docs_indexed += len(list_of_articles)
                else:
                    # When token is not in the search dataset
                    unindexed_word_count += 1
            except KeyError:
                unindexed_word_count += 1
        
        end_time = time.time()  
        search_time = end_time - start_time
        search_time_ns = int(search_time * 1e9)


        
        # Creates DataFrame for missing word count in this dataset
        dataset_df = pd.DataFrame({
            'run_id': run_id,
            'compute_proc_type': compute_proc_type,
            'primary_memory_size': primary_memory_size,
            'index_type': [index_name],
            'dataset': [i + 1],
            'num_docs_indexed': docs_indexed,
            'num_tokens_indexed': [unindexed_word_count],
            'search_set_base_size': [n_list[i]],
            'search_time': [search_time_ns]
        })
        
        # Append to the main DataFrame
        df = pd.concat([df, dataset_df], ignore_index=True)
    
    return df


#E3 - Finding phrases (two words) in a search dataset
def find_phrases_in_datasets(index_name, index, datasets, n_list, run_id, compute_proc_type, primary_memory_size):
    """
    Identifies the number of documents with the exact phrase of words
    """


    df = pd.DataFrame()


    for i in range(len(datasets)):
        # Total num of documents indexed for this dataset
        docs_indexed = 0  
        # Total num of tokens indexed for this dataset   
        tokens_indexed = 0

        # reset total counts of docs and tokens
        total_docs_indexed = 0
        total_tokens_indexed = 0

        start_time = time.time()

        # make a list of phrases from search datasets
        multiple_words = [item for item in datasets[i] if ' ' in item]

        #Iterate through each word in the strings with multiple words
        for phrase in multiple_words:
            words = phrase.split()  # Split the phrase into individual words

            # only search for words in the phrase
            for word in words:


                try:
                    list_of_articles = index.search(word)

                    # If articles are found for the word, add to the respective counters
                    if list_of_articles:
                        docs_indexed += len(list_of_articles)
                        tokens_indexed += 1

                except KeyError:
                    # If the word isn't found in the index, continue with the next word
                    pass

        # Accumulate totals for all datasets
        total_docs_indexed += docs_indexed
        total_tokens_indexed += tokens_indexed

        end_time = time.time()
        search_time = end_time - start_time
        search_time_ns = int(search_time * 1e9)


        # Final dictionary for overall counts
        overall_summary = {
            'run_id': run_id,
            'compute_proc_type': compute_proc_type,
            'primary_memory_size': primary_memory_size,
            'index_type': index_name,
            'dataset': i+1,
            'num_docs_indexed': total_docs_indexed,
            'num_tokens_indexed': total_tokens_indexed,
            'search_set_base_size': n_list[i],
            'search_time': search_time_ns
        }

        # Convert data to a DataFrame (one row)
        new_row = pd.DataFrame([overall_summary])

        # Append the new row to the DataFrame
        df = pd.concat([df, new_row], ignore_index=True)

    return df

def find_search_data_sets(path: str):
    all_search_datasets = []
    all_n = []
    # path should contain the location of the news articles you want to parse
    if path is not None:
        print(f"path = {path}")

    with open(path, 'r', encoding='utf-8') as file:
        entire_json = json.load(file)

    for dict in entire_json:
        # specify dataset key with words
        dataset = dict.get('dataset', [])
        n = dict.get('n', 0)
        all_search_datasets.append(dataset)
        all_n.append(n)
    return all_search_datasets, all_n



def load_index(file_path):
    """
    Load the index from a pickle file.
    """
    with open(file_path, 'rb') as f:
        index = pickle.load(f)
    print(f"Index loaded from {file_path}")
    return index



def main():

    pickle_data_bst = '/Users/Heidi/Downloads/final_pickles/bst_index.pkl'
    pickle_data_avl = '/Users/Heidi/Downloads/final_pickles/avl_index.pkl'
    pickle_data_ht = '/Users/Heidi/Downloads/final_pickles/hash_index.pkl'
    pickle_data_l = '/Users/Heidi/Downloads/final_pickles/list_index.pkl'

    # pickle_data_bst = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\bst_index.pkl'
    # pickle_data_avl = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\avl_index.pkl'
    # pickle_data_ht = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\hash_index.pkl'
    # pickle_data_l = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\list_index.pkl'

    # pickle_data_bst = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/bst_index.pkl'
    # pickle_data_avl = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/avl_index.pkl'
    # pickle_data_ht = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/hash_index.pkl'
    # pickle_data_l = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/list_index.pkl'


    bst_index = load_index(pickle_data_bst)
    avl_index = load_index(pickle_data_avl)
    hash_index = load_index(pickle_data_ht)
    list_index = load_index(pickle_data_l)


    data_directory = '/Users/Heidi/Downloads/compiled_datasets_final.json'
    # data_directory = 'C:\\Users\\lilyh\\Downloads\\experiment_data\\compiled_datasets_final.json'
    # data_directory = '/Users/mihaliskoutouvos/Desktop/Classes/24s-ds4300-koutouvos/practical-01-index_builder/compiled_datasets_final.json'

    # make a list of all the words from search data sets
    datasets, n_list = find_search_data_sets(data_directory)

    # Now perform search experiments
    print("E1 Experiments")
    df1_1 = experiment_searching('list', list_index, datasets, n_list, 1, 'M2', 16)
    df2_1 = experiment_searching('hash', hash_index, datasets, n_list, 1, 'M2', 16)
    df3_1 = experiment_searching('avl', avl_index, datasets, n_list, 1, 'M2', 16)
    df4_1 = experiment_searching('bst', bst_index, datasets, n_list, 1, 'M2', 16)

    exp_1_df_combined = pd.concat([df1_1, df2_1, df3_1, df4_1], axis=0)

    print("E2 Experiments")
    df1_2 = experiment_missing_words('list', list_index, datasets, n_list, 2, 'M2', 16)
    df2_2 = experiment_missing_words('hash', hash_index, datasets, n_list, 2, 'M2', 16)
    df3_2 = experiment_missing_words('avl', avl_index, datasets, n_list, 2, 'M2', 16)
    df4_2 = experiment_missing_words('bst', bst_index, datasets, n_list, 2, 'M2', 16)

    exp_2_df_combined = pd.concat([df1_2, df2_2, df3_2, df4_2], axis=0)

    print("E3 Experiments")
    df1_3 = find_phrases_in_datasets('list', list_index, datasets, n_list, 3, 'M2', 16)
    df2_3 = find_phrases_in_datasets('hash', hash_index, datasets, n_list, 3, 'M2', 16)
    df3_3 = find_phrases_in_datasets('avl', avl_index, datasets, n_list, 3, 'M2', 16)
    df4_3 = find_phrases_in_datasets('bst', bst_index, datasets, n_list, 3, 'M2', 16)
    
    exp_3_df_combined = pd.concat([df1_3, df2_3, df3_3, df4_3], axis=0)


    print('Created dataframes for all indexing structures.')
    print('Concat everything...')

    final_df_combined = pd.concat([exp_1_df_combined, exp_2_df_combined, exp_3_df_combined], axis=0)
    final_df_combined.to_excel('timing_data.xlsx', index=False, sheet_name='sheet1')
    final_df_combined.to_csv('timing_data.csv', index=False)


if __name__ == "__main__":
    main()
