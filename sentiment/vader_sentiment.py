from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import os

# run from sentiment directory

# Initialize VADER so we can use it later
sentimentAnalyser = SentimentIntensityAnalyzer()

pd.options.display.max_colwidth = 400

directory_path = '../csv_files'
data = []

for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        # Read the CSV file and extract its content
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Append the data to the list
        data.append([filename, text])
    
df = pd.DataFrame(data, columns=['college', 'text'])

def calculate_sentiment(text):
    # Run VADER on the text
    scores = sentimentAnalyser.polarity_scores(text)
    # Extract the compound score
    compound_score = scores['compound']
    # Return compound score
    return compound_score

# Apply the function to every row in the "text" column and output the results into a new column "sentiment_score"
df['sentiment_score'] = df['text'].apply(calculate_sentiment)

# Print colleges with the 10 highest sentiment scores
print(df.sort_values(by='sentiment_score', ascending=False)[:10])

# Print colleges with the 10 lowest sentiment scores
print(df.sort_values(by='sentiment_score', ascending=True)[:10])

# TODO: Can do more with region, looking at regions with the highest sentiment etc

# TODO: Visualization stuff
