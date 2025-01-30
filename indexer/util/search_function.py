import json

# Load the JSON file
with open("data.json", "r") as file:
    data = json.load(file)

for file in data:
    # Extract relevant fields
    title = data.get("title", "No title available")
    text = data.get("text", "No text available")
    published_date = data.get("published", "No date available")
    url = data.get("url", "No URL available")

    # Extract preprocessed text
    preprocessed_text = data.get("preprocessed_text", [])

    # Print the extracted information
    print(f"Title: {title}")
    print(f"Published Date