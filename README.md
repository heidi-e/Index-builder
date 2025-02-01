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




### Your Task

Using the sample dataset of finance-related news articles from 2018, you'll build indexes of varying sizes (number of documents) for each of the following data structures:

- Binary Search Tree (BST)
- AVL Tree
- Hash Table
- An indexing data structure of your choice

You'll then run experiments to evaluate the performance of each data structure with respect to searching for a single word and/or a set of words.

After collecting a sufficient amount of data, you'll analyze to draw conclusions about the relative performance of each data structure. You'll make a recommendation to the researcher on which data structure to use for their search engine (with supporting data and analysese) in the form of a research report.

### DataSet

**Link to dataset will be pinned in the class Slack Channel.**

**DO NOT EVER PUT THE DATASET IN YOUR REPO FOLDER. We do NOT want it pushed to GitHub.**

The input corpus is based on the [US Financial News Articles](https://www.kaggle.com/datasets/jeet2016/us-financial-news-articles) Kaggle Dataset. It is a collection of finance-related news articles from Jan - May 2018. Each news article is stored in a separate JSON file containing metadata about the article as well as its full text. The full text has been pre-processed to remove stop words, remove any tokens composed of only digits and decimal points, and lemmatized.

## Requirements

1. Implement indexers based on the template repository using the following data structures:
   - Binary Search Tree (BST)
   - AVL Tree
   - Hash Table
   - An indexing data structure of your choice
1. Crawl the folders of news articles and extract important metadata from each article as well as the `preprocessed_text` element. (Do not index the `text` element.) As you're parsing the new articles, store each word in the indexing structure you are currently testing along with the filename as the value. For the purpose of the project, you should extract, parse, and index the following metadata:
   - title
   - source URL's domain name (cnn.com, reuters.com, etc.)
   - author's last name if present
1. Generate >= 8 searching data sets of varying sizes, each with the following components:
   - **Component A**: a random sample of _n_ terms/tokens currently in the index (n should be a multiple of 4 and >= 4000),
   - **Component B**: an additional _(n/4)_ 2- and 3-word phrases added to the search set by randomly selecting 2 or 3 tokens from Component A and adding them to the searching data set,
   - **Component C**: an addition of _n_ randomly generated strings of characters that are unlikely to be in the index, and
   - **Component D**: an additional _(n/4)_ 2- and 3-word phrases to the set by randomly selecting 2 or 3 tokens from Component C and adding them to the searching data set
   - **Shuffle each of the searching data sets before using them in the experiments below.**
   -
1. Design and implement a set of experiments to evaluate the performance of each data structure with respect to searching for tokens from the searching data sets. Take into consideration the information that is to be included in the final report so that you collect the correct data. For each run of an experiment, measure the time it takes to search the current data structure for the tokens in the searching data sets. Collect the data into a csv file that you will submit with your report.

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

- Your implementation should run with Python 3.11. To create a new conda environment with python 3.11, run the following:

```bash
conda create -n <new_env_name> python=3.11
```

Subsequently, install additional packages listed in the requirements.txt file with:

```bash
pip install -r requirements.txt
```

If you add any packages to the base install, be sure to add them to the `requirements.txt` so the TAs will be able to run your programs easily.

## Final Deliverable

1. A professional GitHub repository with your implementation. It should include a `README.md` file in the root folder giving **clear instructions on how to execute your program**.
2. A CSV file containing the raw collected timing data. It should be stored in the `timing_data` folder of your repository. Your CSV file should be named `timing_data.csv`, and the columns of the CSV file should be the following:
   - `run_id`: a unique id for this run of an experiment. This will help differentiate between runs of the same experiment (you should replicate each experiment multiple times and use the averages of the runs as the final result for that experiment).
   - `compute_proc_type`: Intel i5, i7, or i9; AMD Ryzen 5, 7, or 9; Apple M1, M2, M3, or M4; or other (note this value will be the same for all runs of all experiments for one person on one machine)
   - `primary_memory_size`: the size of the primary memory (RAM) in GB (note this value will be the same for all runs of all experiments for one person on one machine)
   - `index_type`: the type of index used for the experiment (BST, AVL, Hash Table, or the name of the 4th data structure you chose)
   - `num_docs_indexed`: the number of documents (individual JSON files) indexed for this experiment
   - `num_tokens_indexed`: the number of tokens indexed for this experiment
   - `search_set_base_size`: the value of _n_ used when generating this search data set.
   - `search_time`: the time it took to search for the term in nanoseconds
3. The list of documents returned for a specified search set. This should be stored in the `search_results` folder of your repository. I will provide this list to you, including the specific json files to search over. This step is to show that your search is functional.
4. An analysis report in PDF form uploaded to GradeScope by the deadline. It should follow the structure of the template that will be provided to you.
   - Remember, this is a data science course and the analysis performed should be robust and consistent with the level of this course and the skills gained in the prerequisites.
   - There are several variables that you can manipulate in your experiments. Each experiment should only manipulate one variable at a time. Run your experiments in replicate in order to characterize the variability of the data.
   - If you would like to do your data analysis and visualization generation in Jupyter (before writing your report), please include the Notebook file in the `timing_data` folder. Don't forget to add Jupyter/JupyterLab to the `requirements.txt` file. You can install Jupyter/JupyterLab in your environment via `pip install jupyterlab`.
