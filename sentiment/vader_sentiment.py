from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
region_data = ["newengland","newengland","mideast","newengland","newengland","newengland","newengland","newengland","farwest","farwest","plains","mideast","farwest","newengland","mideast","plains","rockymountains","mideast","mideast","mideast","mideast","newengland","greatlakes","southeast","southeast","newengland","mideast","plains","mideast","plains","newengland","farwest","mideast","greatlakes","mideast","southeast","mideast","plains","newengland","newengland","mideast","newengland","greatlakes","farwest","farwest","mideast","newengland","southwest","farwest","mideast","newengland","southeast","farwest","mideast","newengland","southeast","farwest","farwest","farwest","farwest","greatlakes","southeast","greatlakes","southeast","greatlakes","mideast","farwest","southeast","southeast","mideast","mideast","southeast","southeast","plains","mideast","newengland","newengland","newengland","newengland"]
df['region'] = region_data


def calculate_sentiment(text):
    # Run VADER on the text
    scores = sentimentAnalyser.polarity_scores(text)
    # Extract the compound score
    compound_score = scores['compound']
    # Return compound score
    return compound_score

# Apply the function to every row in the "text" column and output the results into a new column "sentiment_score"
df['sentiment_score'] = df['text'].apply(calculate_sentiment)
asc_sorted_df = df.sort_values(by='sentiment_score', ascending=True)
desc_sorted_df = df.sort_values(by='sentiment_score', ascending=False)
# Print colleges with the 10 highest sentiment scores
#print(desc_sorted_df[:10])

# Print colleges with the 10 lowest sentiment scores
#(asc_sorted_df[:10])

# TODO: Can do more with region, looking at regions with the highest sentiment etc

# Group the DataFrame by 'region' and calculate the mean sentiment score for each region
region_sentiment_mean = df.groupby('region')['sentiment_score'].mean().reset_index()

# Sort the DataFrame by the mean sentiment score in descending order to get the highest sentiment scores
highest_sentiment_regions = region_sentiment_mean.sort_values(by='sentiment_score', ascending=False)

# Print regions with the highest sentiment scores
print("Regions with the highest sentiment scores:")
print(highest_sentiment_regions)

# TODO: Visualization stuff

# Sentiment distribution visualization 
plt.figure(figsize=(10, 6))
sns.histplot(df['sentiment_score'], bins=30, kde=True)
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Explore correlation with the length of the text
df['text_length'] = df['text'].apply(len)
correlation = df[['sentiment_score', 'text_length']].corr().iloc[0, 1]
print(f"Correlation between sentiment score and text length: {correlation}")

# Compare sentiment scores among different regions using a boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(x='region', y='sentiment_score', data=df)
plt.title('Sentiment Scores by Region')
plt.xlabel('Region')
plt.ylabel('Sentiment Score')
plt.show()

# Analyze sentiment scores based on predefined thresholds (positive, neutral, negative)
thresholds = {'positive': 0.05, 'negative': -0.05}
df['sentiment_category'] = pd.cut(df['sentiment_score'], bins=[-float('inf'), thresholds['negative'], thresholds['positive'], float('inf')], labels=['negative', 'neutral', 'positive'])
sentiment_counts = df['sentiment_category'].value_counts()
print("Sentiment Category Distribution:")
print(sentiment_counts)

# Compare sentiment categories across regions
region_sentiment_counts = df.groupby(['region', 'sentiment_category']).size().unstack().fillna(0)
print("Sentiment Category Distribution by Region:")
print(region_sentiment_counts)
