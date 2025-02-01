# DS4300 - Spring 2025 - Practical #1 - Index It

## Group: 
Heidi Eren, Lily Hoffman, and Mihalis Koutouvos

## Assignment Overview: 

### Scenario (Hypothetical):

You're working for a researcher who is trying to build a specialized search engine over a large corpus of documents. The researcher ultimately need a fast way to search through thousands of documents for specific words or phrases and the total number of documents that contain the word or phrase and total number of pre-processed words in those documents.

The first step is to evaluate the performance of several different in-memory indexing data structures so that you can make an informed decision on which data structure to use. The researcher has provided you with a dataset of news articles and asked you to evaluate the performance of the data structures with respect to searching.

Good news - you'll benefit from the work of the previous research assistant who just accepted a co-op. The had already implemented the bulk of the BST, a portion of the AVL tree, and has set up a repository already!

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
1. My group started off by doing one of the data structures a person. 
2. From here, we decided to set up the info for the experiments and also start the indexing process via crawling the folders, extracting relevant metadata such as `preprocessed_text`.
3. As we went about parsing, our function stored each word in the index structure we were testing along with its filename. 
4. The following metadata was manipulated:
   - title
   - source URL's domain name (cnn.com, reuters.com, etc.)
   - author's last name if present
5. We proceeded to generate around 9 searching data sets of varying sizes, each with the following components:
   - **Component A**: a random sample of _n_ terms/tokens currently in the index (n should be a multiple of 4 and >= 4000),
   - **Component B**: an additional _(n/4)_ 2- and 3-word phrases added to the search set by randomly selecting 2 or 3 tokens from Component A and adding them to the searching data set,
   - **Component C**: an addition of _n_ randomly generated strings of characters that are unlikely to be in the index, and
   - **Component D**: an additional _(n/4)_ 2- and 3-word phrases to the set by randomly selecting 2 or 3 tokens from Component C and adding them to the searching data set
   - **We also shuffled each of the searching data sets before using them in the experiments.**
   

## Implementation Details and Considerations

- I have included a decorator in `indexer.util.timer` that tracks the execution time of a function in nanoseconds and milliseconds. You are free to use it directly or modify it for your needs. OR, you can implement your own timer function to track performance data in some other Pythonic way if you'd like.

- You'll use the following data structures as indexes for this project:
  - Binary Search Tree (already implemented for you, but you can modify it if you'd like)
  - AVL Tree (started for you)
  - Hash Table (custom implementation, primary functions stubbed out for you. Don't simply use a Python dictionary.)
  - A 4th indexing data structure of your choice
- You can modify the nodes of each of the data structures to include additional data if you'd like.

- File Storage/Locations:
  
  - None of our datasets are in our repo for the sake of saving storage and time. Instead, we stored our indexed one in a pickle file for use in the experiments. 
  - Our pickle files are also not in the repo for similar reason. The path to the root folder of the dataset is currently a variable in `assign_01.py`. You should convert this to a command line argument that can be passed in when running the program.
    - For example: `-d` or `--dataset` 
  - We also pickled our indexes, so we have  a separate command line argument for the path to the pickle files.
    - For example: `-p` or `--pickle` 

- Each of the data structures inherit from a common interface of functionality in `indexer.abstract_index.AbstractIndex`. 

### Python Environment

- Our implementation runs with Python 3.11. To create a new conda environment with python 3.11, run the following:

```bash
conda create -n <new_env_name> python=3.11
```

Subsequently, install additional packages listed in the requirements.txt file with:

```bash
pip install -r requirements.txt
```