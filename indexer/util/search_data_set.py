import random
import string

def multi_phrase(n, comp_letter):
    '''
    To create components with addition of (n/4) 2- and 3-word phrases
    by randomly selecting 2 or 3 tokens from Input Component and adding
    them to the searching data set
    '''

    m = (n / 4)
    rand_selected_from_comp = " ".join(random.sample(comp_letter, random.choice([2, 3])))

    return [rand_selected_from_comp for _ in range(m)]



def create_search_data_set(index_struc, n: int, file_path):

    #Figure out the components:
    #Component A:
    if n % 4 != 0 or n < 4000:
        raise ValueError("n has to have a remainder of 4 and be at least 4000")


    # Component A
    # Randomly sample n terms currently in index
    all_terms = index_struc.get_keys_in_order(file_path)
    comp_A = random.sample(all_terms, n)


    # Component B
    # (n/4) two- and three-word phrases from Component A
    comp_B = multi_phrase(comp_A, n)


    # Component C
    # n random string of words not in index
    length = random.randint(5, 10)
    comp_C_selected = ''.join(random.choices(string.ascii_lowercase, k=length))
    comp_C = [comp_C_selected for _ in range(n)]

    # Component D
    # (n/4) two- and three-word phrases from Component C
    comp_D = multi_phrase(comp_C, n)



    # combine and shuffle components
    combine_comps = comp_A + comp_B + comp_C + comp_D
    random.shuffle(combine_comps)

    return combine_comps