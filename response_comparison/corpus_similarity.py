from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
import os
import pandas as pd

# This program tokenizes and vectorizes the corpus in order to find the cosine_similarity between different documents
# Cosine similarity is a measure of similarity between two non-zero
# vectors of an inner product space that measures the cosine of the angle between them

# Higher values indicate greater similarity between documents, while lower values indicate lower similarity

# To find the similarity between the first document and the second document, you would look at the value in the 
# first row and second column (or vice versa)

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Set up NLTK stopwords
stop_words = set(stopwords.words('english'))

directory_path = '../csv_files'

# Function to preprocess text
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word.translate(translator) for word in tokens]
    return " ".join(tokens)

# Read CSV files and extract text data
documents = []
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory_path, filename)
        df = pd.read_csv(filepath, names=['Text']) 
        text_column = df['Text'].astype(str)  
        for text in text_column:
            documents.append(preprocess(text))

# Convert text to vectors using CountVectorizer (Bag of Words)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# https://www.geeksforgeeks.org/python-measure-similarity-between-two-sentences-using-cosine-similarity/
# Calculate cosine similarity
similarity_matrix = cosine_similarity(X)

# Output similarity matrix
print(similarity_matrix)

# Can definitely do more such as seeing highest similarities etc
