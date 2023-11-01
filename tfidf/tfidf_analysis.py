import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# run from tfidf directory
folder_path = '../csv_files'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

corpus = []

# create our corpus of texts from our csv files
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            corpus.append(text)

# THE BELOW CODE PRODUCES OUR TFIDF VECTORS AND OUTPUTS INTO CSV - DOES NOT NEED TO BE RERUN (LONG RUNTIME)
# WE JUST LOAD FROM CSV AND WORK WITH THE LOADED DF

#df = pd.DataFrame({'text': corpus})

#tfidf_vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
#tfidf_matrix = tfidf_vectorizer.fit_transform(df['text'])

#tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

#data = []
#for row_index, row in tfidf_df.iterrows():
    #document = csv_files[row_index]  # The document index
    #for col_index, tfidf_score in enumerate(row):
        #word = tfidf_vectorizer.get_feature_names_out()[col_index]  # Get the word based on the column index
        #data.append([document, word, tfidf_score])

#tfidf_data_df = pd.DataFrame(data, columns=['document', 'word', 'tfidf score'])

#output_csv_path = 'tfidf_vectors.csv'
#tfidf_data_df.to_csv(output_csv_path, index=False)

# load csv and remove rows with 0 tf-idf scores
tfidf_data_df = pd.read_csv('tfidf_vectors.csv')
tfidf_data_df = tfidf_data_df[tfidf_data_df['tfidf score'] != 0.0]  

print(tfidf_data_df)



