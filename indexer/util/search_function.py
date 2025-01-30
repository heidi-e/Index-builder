import json


def crawl_data(index_struct, file_path):
    """
    Crawl folders of news articles and extract metadata
    Args:
        index_struct: index structure you are testing
        file_path: path to the folder containing the dataset

    Returns:

    """

    # Load the JSON file
    with open(file_path, "r") as f:
        data = json.load(f)

    for file in data:

        # Extract relevant fields
        title = file["title"]
        url = file['url']
        if file['author'] != "":
            author = file['author'].split('')[1]

        # Extract preprocessed text
        raw_preprocessed_text = file["preprocessed_text"]

        # store into indexing structure
        for word in raw_preprocessed_text:
            index_struct.insert(word, file)
            index_struct.insert(word, title)
            index_struct.insert(word, url)
            index_struct.insert(word, author)


