import random
import string
import pickle
import time
import json

def generate_n():
    """Generates a random integer n that is less than or equal to 4000 and divisible by 4."""
    return random.randrange(4, 4000, 4)


def multi_phrase(comp_letter, n):
    '''
    To create components with addition of (n/4) 2- and 3-word phrases
    by randomly selecting 2 or 3 tokens from Input Component and adding
    them to the searching data set
    '''
    m = int(n / 4)
    return [" ".join(random.sample(comp_letter, random.choice([2, 3]))) for _ in range(m)]


def create_search_data_set(pickled_indexed_data, n: int):

    # load the pickled data
    indexed_data = load_index(pickled_indexed_data)

    # Component A
    # Randomly sample n terms currently in index
    all_terms = indexed_data.get_keys_in_order()



    comp_A = random.sample(all_terms, n)

    # Component B
    # (n/4) two- and three-word phrases from Component A
    comp_B = multi_phrase(comp_A, n)

    # Component C
    # n random string of words not in index
    comp_C = [''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))) for _ in range(n)]

    # Component D
    # (n/4) two- and three-word phrases from Component C
    comp_D = multi_phrase(comp_C, n)

    # combine and shuffle components
    combined_comps = comp_A + comp_B + comp_C + comp_D
    random.shuffle(combined_comps)

    return combined_comps


def load_index(file_path):
    """
    Load the index from a pickle file.
    """
    with open(file_path, 'rb') as f:
        index = pickle.load(f)
    print(f"Index loaded from {file_path}")
    return index

def reformat_dataset(index, search_data_set, n, time, count):
    """
    Save and compile each dataset as a json file with metrics
    """

    json_dataset = {
            'count': count,
            'dataset': search_data_set,
            'indexing_structure': index,
            'n': n,
            'time': time
        }
    return json_dataset



def main():
    # in command line: python -m indexer.util.search_data_set

    indexing_list = ['hash', 'avl', 'list', 'bst']


    # set file path to save compiled doc
    file_path = "compiled_datasets_final.json"

    # create a new JSON file or open an existing one
    try:
        with open(file_path, "r") as file:
            dataset_file = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        dataset_file = []  # Create an empty list if file doesn't exist or is empty


    # generate data sets and compile them into one json file
    for i in range(8):

        start_time = time.time()
        # generate a random sample n to token
        n = generate_n()

        # select a random indexing structure
        random_idx = random.choice(indexing_list)

        # specify directory with pickled indexing structure
        index_data = f'/Users/Heidi/Downloads/final_pickles/{random_idx}_index.pkl'

        # generate searching data set
        search_data_set = create_search_data_set(index_data, n)

        end_time = time.time()

        # compile into json file
        tot_time = round(end_time - start_time, 2)
        reformated_data = reformat_dataset(random_idx, search_data_set, n, tot_time, i+1)

        dataset_file.append(reformated_data)

    # write updated data to the JSON file
    with open(file_path, "w") as file:
        json.dump(dataset_file, file, indent=4)



if __name__ == '__main__':
    main()