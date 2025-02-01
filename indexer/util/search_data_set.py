import random
import string
import pickle
from indexer.maps.hash_map import HashMapIndex

def generate_n():
    """Generates a random integer n that is at least 4000 and divisible by 4."""
    return random.randrange(4000, 10000, 4)


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

    #print(indexed_data[:5])
    # Check if there are enough terms to sample from
    #if len(all_terms) < n:
        #raise ValueError("Sample size 'n' is larger than the number of unique terms in the index")
    
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


def main():
    # in command line: python -m indexer.util.search_data_set

    # generate random number n
    n = generate_n()

    # test with 12 for now
    #n = 12


    #hash_indexer = 'C:\\Users\\lilyh\\Downloads\\pickles\\pickles\\hash_index.pkl'

    # specify directory with pickled indexing structure
    #bst_index_data = '/Users/Heidi/Downloads/pickles/bst_index.pkl'
    #lst_index_data = '/Users/Heidi/Downloads/pickles/list_index.pkl'
    #hash_index_data = '/Users/Heidi/Downloads/pickles/hash_index.pkl'
    avl_index_data = '/Users/Heidi/Downloads/pickles/avl_index.pkl'

    # generate searching data set
    search_data_set = create_search_data_set(avl_index_data, n)

    print(search_data_set)

if __name__ == '__main__':
    main()