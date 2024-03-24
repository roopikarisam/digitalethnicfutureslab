import os
import pandas as pd
from nltk import ngrams, FreqDist, word_tokenize
from nltk.corpus import stopwords
import string
import nltk

# ngram_analysis.py performs n-gram analysis on the corpus of text files
# defines functions to preprocess text, tokenize them, then find top n-grams which are stored in a list then converted
# into a df

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Set up NLTK stopwords
stop_words = set(stopwords.words('english'))

directory_path = '../csv_files'

# Initialize an empty list to store results
results_list = []

# preprocess and tokenize text
def pre_process(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# perform actual analysis
def ngram_analysis(tokens, n):
    n_grams = ngrams(tokens, n)
    # Filter out n-grams containing punctuation
    n_grams_no_punct = [gram for gram in n_grams if all(word.isalnum() or word in string.whitespace for word in gram)]
    return FreqDist(n_grams_no_punct)


# Iterate through CSV files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        
        # Read the content of CSV file
        with open(file_path, 'r', encoding='utf-8') as file:
            corpus = file.read()
        
        # Preprocess and tokenize
        tokens = pre_process(corpus)
        
        # Specify the desired n for n-grams (e.g., 2 for bigrams)
        # Currently set to trigrams
        n = 3
        
        # Perform n-gram analysis
        ngram_freq_dist = ngram_analysis(tokens, n)
        
        # Get the top 10 n-grams
        top_ngrams = ngram_freq_dist.most_common(10)
        
        # Append results to the list
        results_list.append({'Filename': filename, 'Top N-grams': top_ngrams})

# Create a DataFrame from the list
results_df = pd.DataFrame(results_list)

# Display the results DataFrame
print(results_df)
