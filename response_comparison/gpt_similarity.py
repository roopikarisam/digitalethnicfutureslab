import csv
import os
from nltk.tokenize import word_tokenize

# This program tokenizes text (both a GPT response and text from our corpus) in order to perform Jaccard 
# similarity comparison
# https://www.learndatasci.com/glossary/jaccard-similarity/#:~:text=The%20Jaccard%20similarity%20measures%20the,of%20observations%20in%20either%20set.

csv_directory = '../csv_files'
text_to_compare = 'GPT.csv'

# Function to read the contents of a CSV file and tokenize the text
def read_csv_and_tokenize(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Assuming the text is in the first column of the CSV file
        text_column = next(reader)
        text = ' '.join(text_column)
        tokens = word_tokenize(text.lower())  # Tokenize the text and convert to lowercase
        return set(tokens)  # Convert tokenized text to a set of tokens

# Function to compute Jaccard similarity between two sets of tokens
def compute_jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Tokenize the text to compare
text_to_compare_tokens = read_csv_and_tokenize(text_to_compare)

# Calculate similarity for each file in the directory
similarity_scores = []
for filename in os.listdir(csv_directory):
    file_path = os.path.join(csv_directory, filename)
    if os.path.isfile(file_path):
        file_content_tokens = read_csv_and_tokenize(file_path)
        similarity = compute_jaccard_similarity(text_to_compare_tokens, file_content_tokens)
        similarity_scores.append((filename, similarity))

# Sort similarity scores in descending order
similarity_scores.sort(key=lambda x: x[1], reverse=True)

# Print the top similar files
print("Top similar files:")
for file, score in similarity_scores[:5]:
    print(f"File: {file}, Similarity Score: {score}")