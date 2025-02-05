# DS4300 - Spring 2025 - Practical #1 - Index Builder

## Group: 
Heidi Eren, Lily Hoffman, and Mihalis Koutouvos

## Running Program: 
- In order to run the program, please clone the repository and proceed with the following steps. Please also be sure to run the experiments.py file, which is inside of util. 

### Python Environment

- Our implementation runs with Python 3.11. To create a new conda environment with python 3.11, run the following:

```bash
conda create -n <new_env_name> python=3.11
```

Subsequently, install additional packages listed in the requirements.txt file with:

```bash
pip install -r requirements.txt
```

- The above steps should allow you to run the program successfully. Also, to run commands, please use the terminal system rather than clicking run. We used VSCode for our program.

## Assignment Overview: 

### Scenario (Hypothetical):

You're working for a researcher who is trying to build a specialized search engine over a large corpus of documents. The researcher ultimately needs a fast way to search through thousands of documents for specific words or phrases and the total number of documents that contain the word or phrase and total number of pre-processed words in those documents.

The first step is to evaluate the performance of several different in-memory indexing data structures so that you can make an informed decision on which data structure to use. The researcher has provided you with a dataset of news articles and asked you to evaluate the performance of the data structures with respect to searching.

Good news - you'll benefit from the work of the previous research assistant who just accepted a co-op. They had already implemented the bulk of the BST, a portion of the AVL tree, and has set up a repository already!

### Due Dates:
- EC Due Date: February 2nd, 2025 @ 11:59pm
- Regular Due Date: February 4th, 2025 @ 11:59pm

## Important Notes:

- [ ] What did we submit? 
  - [ ] The implementation for our project submitted through GitHub/GH Classroom.
  - [ ] A written portion representing our project report via Gradescope

### DataSet
The input corpus is based on the [US Financial News Articles](https://www.kaggle.com/datasets/jeet2016/us-financial-news-articles) Kaggle Dataset. It is a collection of finance-related news articles from Jan - May 2018. Each news article is stored in a separate JSON file containing metadata about the article as well as its full text. The full text has been pre-processed to remove stop words, remove any tokens composed of only digits and decimal points, and lemmatized.


## Implementation Procedure:
1. Our group started off by doing one of the data structures a person. 
2. From here, we decided to set up the info for the experiments and also start the indexing process via crawling the folders, extracting relevant metadata such as `preprocessed_text`.
3. As we went about parsing, our function stored each word in the index structure we were testing along with its filename. 
4. The following metadata was manipulated:
   - title
   - source URL's domain name (cnn.com, reuters.com, etc.)
   - author's last name if present
5. We proceeded to generate 8 [searching data sets](https://github.com/user-attachments/files/18636051/compiled_datasets.json) of varying sizes, each with the following components:
   - **Component A**: a random sample of _n_ terms/tokens currently in the index (n should be a multiple of 4 and >= 4000),
   - **Component B**: an additional _(n/4)_ 2- and 3-word phrases added to the search set by randomly selecting 2 or 3 tokens from Component A and adding them to the searching data set,
   - **Component C**: an addition of _n_ randomly generated strings of characters that are unlikely to be in the index, and
   - **Component D**: an additional _(n/4)_ 2- and 3-word phrases to the set by randomly selecting 2 or 3 tokens from Component C and adding them to the searching data set
   - **We also shuffled each of the searching data sets before using them in the experiments.**
   

## Implementation Details and Considerations
- File Storage/Locations:
  
  - None of our datasets are in our repo for the sake of saving storage and time. Instead, we stored our indexed one in a pickle file for use in the experiments. 
  - Our pickle files are also not in the repo for similar reason ([Download Zip File](https://drive.google.com/uc?export=download&id=1k8zua3W_LVEDGBLF-HjJ2N8ALh9_QuDG)). They are stored locally and called through the local path containing the root folder of new articles files dataset (USFinancialNewsArticles-preprocessed). You should convert this to a command line argument that can be passed in when running the program.
    - For example: `-d` or `--dataset` 
  - We also pickled our indexes, so we have a separate command line argument for the path to save the pickle files.
    - For example: `-p` or `--pickle` 
  - Navigate to the project root directory then run the search function module from the command line, specifying the dataset directory and the output path for the pickled index.
    - `python -m indexer.util.search_function -d /path/to/dataset -p /path/to/output/index.pkl`
  
  - To create the search data sets and save into a json file, run the script from the command line. 
    - `python -m indexer.util.search_data_set`

  - To run the experiments and save the results into a csv or Excel file, run the script from the command line. Make sure to set the correct root directories for the pickled indexes and search datasets.
    - `python -m indexer.util.exp`
    
- Each of the data structures inherit from a common interface of functionality in `indexer.abstract_index.AbstractIndex`.
