import random


def create_search_data_set(index_struc, n: int, file_path):

    #Figure out the componets:
    #Component A:
    if n % 4 != 0 or n < 4000:
        raise ValueError("n has to have a remainder of 4 and be at least 4000")
    
    




    #All the components and their requirements:
    comp_A = []
    comp_B = []
    comp_C = []
    comp_D = []

    combine_comps = comp_A + comp_B + comp_C + comp_D
    random.shuffle(combine_comps)

    return 