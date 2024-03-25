import pandas as pd
from collections import Counter
import os
import string
import nltk
from nltk.corpus import stopwords

# Download NLTK stop words (if not already downloaded)
nltk.download('stopwords')

# Define stop words set
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Function to calculate average word count, lexical diversity, and most frequent words
def analyze_csv_files(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    results = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            print(f"Processing file: {file_name}")
            df = pd.read_csv(os.path.join(folder_path, file_name), header=None)
            for text in df[0]:
                text = preprocess_text(str(text))
                words = text.split()

                # Calculate lexical diversity (Type-Token Ratio)
                # Lexical density is a measure of the proportion of content words (nouns, verbs, adjectives, and adverbs) in a text compared to the total number of words
                ttr = len(set(words)) / len(words) if len(words) > 0 else 0

                # Filter out stop words from word list
                words = [word for word in words if word not in stop_words]

                # First 19 words are stopwords that are filtered out, we use 69 to get the 50 most common non stop words
                word_freq_counter = Counter(words)
                most_common_words = word_freq_counter.most_common(69)

                # Append results to list
                results.append({
                    'File': file_name,
                    'Average Word Count': len(words),
                    'Lexical Diversity (TTR)': ttr,
                    'Most Common Words': most_common_words
                })

    return pd.DataFrame(results)

folder_path = 'csv_files'
output_file = 'word_analysis_results.csv'
try:
    results = analyze_csv_files(folder_path)
    #results.to_csv(output_file, index=False)
    print(results)
except FileNotFoundError as e:
    print(e)

# Calculate and print statistics of lexical diversity
lexical_diversity_values = results['Lexical Diversity (TTR)']
average_ttr = lexical_diversity_values.mean()
highest_ttr = lexical_diversity_values.nlargest(10).tolist()
lowest_ttr = lexical_diversity_values.nsmallest(10).tolist()
median_ttr = lexical_diversity_values.median()

print(f"Average Lexical Diversity (TTR): {average_ttr}")
print(f"5 Highest Lexical Diversity (TTR): {highest_ttr}")
print(f"5 Lowest Lexical Diversity (TTR): {lowest_ttr}")
print(f"Median Lexical Diversity (TTR): {median_ttr}")