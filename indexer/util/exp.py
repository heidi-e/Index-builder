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
    # Initialize counters for the final counts
    total_docs_indexed = 0
    total_tokens_indexed = 0

    df = pd.DataFrame()


    for i in range(len(datasets)):  
        docs_indexed = 0      # Total num of documents indexed for this dataset
        tokens_indexed = 0    # Total num of tokens indexed for this dataset
        start_time = time.time() 

        for word in datasets[i]:   
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

        # Final dictionary for overall counts
        overall_summary = {
            'indexing': index_name,
            'dataset': i+1,
            'n': n_list[i],
            'total_docs_indexed': total_docs_indexed,
            'total_tokens_indexed': total_tokens_indexed,
             'search_time (in seconds)': round(search_time, 6),
             'run_id': run_id,
             'compute_proc_type': compute_proc_type,
             'primary_memory_size': primary_memory_size
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
        start_time = time.time() 
        
        for word in dataset:
            try:
                # When token is not in the search dataset
                if not index.search(word): 
                    unindexed_word_count += 1
            except KeyError:
                unindexed_word_count += 1  
        
        end_time = time.time()  
        search_time = end_time - start_time 
        
        # Creates DataFrame for missing word count in this dataset
        dataset_df = pd.DataFrame({
            'indexing': [index_name],
            'dataset': [i + 1],
            'n': [n_list[i]],
            'unindexed_word_count': [unindexed_word_count],
            'search_time (in seconds)': [search_time],
            'run_id': run_id,
             'compute_proc_type': compute_proc_type,
             'primary_memory_size': primary_memory_size 
        })
        
        # Append to the main DataFrame
        df = pd.concat([df, dataset_df], ignore_index=True)
    
    return df


#E3 - Finding phrases (two words) in a search dataset
def find_phrases_in_datasets(index_name, index, datasets, n_list, run_id, compute_proc_type, primary_memory_size):
    """
    Identifies the number of documents with the exact phrase of words
    """
    total_docs_indexed = 0
    total_tokens_indexed = 0

    df = pd.DataFrame()


    for i in range(len(datasets)):  
        # Total num of documents indexed for this dataset
        docs_indexed = 0  
        # Total num of tokens indexed for this dataset   
        tokens_indexed = 0   
        
        multiple_words = [item for item in datasets if ' ' in item]

        #Iterate through each word in the strings with multiple words
        for phrase in multiple_words:
            words = phrase.split()  # Split the phrase into individual words
            for word in words:
                print(word)

        start_time = time.time() 



        for word in datasets[i]:   
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

        # Final dictionary for overall counts
        overall_summary = {
            'indexing': index_name,
            'dataset': i+1,
            'n': n_list[i],
            'total_docs_indexed': total_docs_indexed,
            'total_tokens_indexed': total_tokens_indexed,
             'search_time (in seconds)': round(search_time, 6),
            'run_id': run_id,
             'compute_proc_type': compute_proc_type,
             'primary_memory_size': primary_memory_size 
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



def my_load_index(file_path):
    """
    Load the index from a pickle file.
    """
    with open(file_path, 'rb') as f:
        index = pickle.load(f)
    print(f"Index loaded from {file_path}")
    return index



def main():

    # pickle_data_bst = '/Users/Heidi/Downloads/final_pickles/bst_index.pkl'
    # pickle_data_avl = '/Users/Heidi/Downloads/final_pickles/avl_index.pkl'
    # pickle_data_ht = '/Users/Heidi/Downloads/final_pickles/hash_index.pkl'
    # pickle_data_l = '/Users/Heidi/Downloads/final_pickles/list_index.pkl'

    pickle_data_bst = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\bst_index.pkl'
    pickle_data_avl = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\avl_index.pkl'
    pickle_data_ht = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\hash_index.pkl'
    pickle_data_l = 'C:\\Users\\lilyh\\Downloads\\final_pickles_results\\final_pickles\\list_index.pkl'

    # pickle_data_bst = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/bst_index.pkl'
    # pickle_data_avl = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/avl_index.pkl'
    # pickle_data_ht = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/hash_index.pkl'
    # pickle_data_l = '/Users/mihaliskoutouvos/Downloads/final_pickles 3/list_index.pkl'


    bst_index = my_load_index(pickle_data_bst)
    avl_index = my_load_index(pickle_data_avl)
    hash_index = my_load_index(pickle_data_ht)
    list_index = my_load_index(pickle_data_l)


    # data_directory = '/Users/Heidi/Downloads/compiled_datasets_final.json'
    data_directory = 'C:\\Users\\lilyh\\Downloads\\experiment_data\\compiled_datasets_final.json'
    # data_directory = '/Users/mihaliskoutouvos/Desktop/Classes/24s-ds4300-koutouvos/practical-01-index_builder/compiled_datasets_final.json'

    # make a list of all the words from search data sets
    datasets, n_list = find_search_data_sets(data_directory)

    # Now perform search experiments
    # print("E1 Experiments")
    # df1 = experiment_searching('list', list_index, datasets, n_list, 1, 'Intel i5', 16)
    # df2 = experiment_searching('hash', hash_index, datasets, n_list, 1, 'Intel i5', 16)
    # df3 = experiment_searching('avl', avl_index, datasets, n_list, 1, 'Intel i5', 16)
    # df4 = experiment_searching('bst', bst_index, datasets, n_list, 1, 'Intel i5', 16)


    #print("E2 Experiments")
    # df1 = experiment_missing_words('list', list_index, datasets, n_list)
    # df2 = experiment_missing_words('hash', hash_index, datasets, n_list)
    # df3 = experiment_missing_words('avl', avl_index, datasets, n_list)
    # df4 = experiment_missing_words('bst', bst_index, datasets, n_list)

    # df1 = experiment_missing_words('list', list_index, datasets, n_list, 2, 'Intel i5', 16)
    # df2 = experiment_missing_words('hash', hash_index, datasets, n_list, 2, 'Intel i5', 16)
    # df3 = experiment_missing_words('avl', avl_index, datasets, n_list, 2, 'Intel i5', 16)
    # df4 = experiment_missing_words('bst', bst_index, datasets, n_list, 2, 'Intel i5', 16)

    print("E3 Experiments")
    #df1 = experiment_missing_words('list', list_index, datasets, n_list)
    #df2 = experiment_missing_words('hash', hash_index, datasets, n_list)
    #df3 = experiment_missing_words('avl', avl_index, datasets, n_list)
    #df4 = experiment_missing_words('bst', bst_index, datasets, n_list)

    # df1 = experiment_missing_words('list', list_index, datasets, n_list, 3, 'Intel i5', 16)
    # df2 = experiment_missing_words('hash', hash_index, datasets, n_list, 3, 'Intel i5', 16)
    # df3 = experiment_missing_words('avl', avl_index, datasets, n_list, 3, 'Intel i5', 16)
    # df4 = experiment_missing_words('bst', bst_index, datasets, n_list, 3, 'Intel i5', 16)

    # df1 = find_phrases_in_datasets('list', list_index, datasets, n_list)
    # df2 = find_phrases_in_datasets('hash', hash_index, datasets, n_list)
    # df3 = find_phrases_in_datasets('avl', avl_index, datasets, n_list)
    # df4 = find_phrases_in_datasets('bst', bst_index, datasets, n_list)

    df1 = find_phrases_in_datasets('list', list_index, datasets, n_list, 3, 'Intel i5', 16)
    df2 = find_phrases_in_datasets('hash', hash_index, datasets, n_list, 3, 'Intel i5', 16)
    df3 = find_phrases_in_datasets('avl', avl_index, datasets, n_list, 3, 'Intel i5', 16)
    df4 = find_phrases_in_datasets('bst', bst_index, datasets, n_list, 3, 'Intel i5', 16)
#
    # print(df2)
    df_combined = pd.concat([df1, df2, df3, df4], axis=0)
    df_combined.to_excel('output_exp3.xlsx', index=False, sheet_name='sheet1')
    
    #print(df3)
    #print(df4)

    #experiment_search_existing(avl_index, datasets)
    #experiment_search_existing(hm_index, datasets)
    #experiment_search_existing(l_index, datasets)
'''
    # Now perform search experiments
    print("E2 Experiments")
    experiment_search_non_existing(bst_index, 100)
    experiment_search_non_existing(avl_index, 100)
    experiment_search_non_existing(hm_index, 100)
    experiment_search_non_existing(l_index, 100)'''


if __name__ == "__main__":
    main()












if __name__ == "__main__":
    main()