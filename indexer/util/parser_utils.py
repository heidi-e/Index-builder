
from typing import List
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
#import indexer.util.nltk_modules as nltk_modules
import nltk
nltk.download('stopwords')

import nltk

def init_nltk_modules():
    try:
        # Attempt to find the resources, if not found, download them.
        nltk.data.find("stopwords")
    except LookupError:
        nltk.download("stopwords", quiet=True)

    try:
        nltk.data.find("wordnet")
    except LookupError:
        nltk.download("wordnet", quiet=True)

    try:
        nltk.data.find("omw-1.4")
    except LookupError:
        nltk.download("omw-1.4", quiet=True)




def preprocess_text(text: str) -> List[str]:
  """
  Preprocesses the given text by performing the following steps:
  1. Splits the text into words.
  2. Lemmatizes each word.
  3. Removes punctuation from each word.
  4. Removes tokens composed of only digits or digits + decimal points.
  5. Removes stop words.
  Args:
    text (str): The input text to be preprocessed.
  Returns:
    List[str]: The list of preprocessed tokens.
  """
  # Call helper function to initialize nltk modules
  init_nltk_modules()
  
  # Split the text into words
  words = text.split()

  # Initialize the lemmatizer
  lemmatizer = WordNetLemmatizer()

  # Initialize the set of stop words
  stop_words = set(stopwords.words('english'))

  # Initialize the set of punctuation
  punctuation = set(string.punctuation)

  # Initialize the list to store the preprocessed tokens
  preprocessed_tokens = []

  # Iterate over each word
  for word in words:
    # Lemmatize the word
    lemma = lemmatizer.lemmatize(word.lower())

    # Remove punctuation
    lemma = ''.join(char for char in lemma if char not in punctuation)

    # Remove tokens composed of only digits or digits + decimal points
    if not lemma.replace('.', '', 1).isdigit():
      # Remove stop words
      if lemma.lower() not in stop_words:
        preprocessed_tokens.append(lemma)

  return preprocessed_tokens
