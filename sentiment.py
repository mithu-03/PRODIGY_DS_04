import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords

# Define column names
column_names = ['ID', 'Entity', 'Sentiment', 'Tweet']

# Load the training and validation data with proper headers
train_data = pd.read_csv('twitter_training.csv', header=None, names=column_names)
validation_data = pd.read_csv('twitter_validation.csv', header=None, names=column_names)

# Preview cleaned data
print("Cleaned Training Data:")
print(train_data.head())

print("\nCleaned Validation Data:")
print(validation_data.head())

# Check for missing values
print("\nMissing Values in Training Data:")
print(train_data.isnull().sum())

print("\nMissing Values in Validation Data:")
print(validation_data.isnull().sum())

# Remove rows with missing tweets from training data
train_data = train_data.dropna(subset=['Tweet'])

# Confirm no missing values now
print("\nAfter dropping missing tweets:")
print(train_data.isnull().sum())

# Count of each sentiment in training data
sentiment_counts = train_data['Sentiment'].value_counts()

# Plotting the sentiment distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
plt.title("Sentiment Distribution in Training Data")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.tight_layout()
plt.savefig("sentiment_distribution.png", dpi=300)
plt.show()


nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_tweet(tweet):
    # Lowercase the tweet
    tweet = tweet.lower()
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    # Remove mentions, hashtags, and reserved words
    tweet = re.sub(r'\@\w+|\#|\brt\b', '', tweet)
    # Remove punctuation and numbers
    tweet = re.sub(r'[^a-zA-Z\s]', '', tweet)
    # Remove stopwords
    tweet = ' '.join([word for word in tweet.split() if word not in stop_words])
    return tweet

# Apply preprocessing to tweets in training and validation sets
train_data['Clean_Tweet'] = train_data['Tweet'].apply(preprocess_tweet)
validation_data['Clean_Tweet'] = validation_data['Tweet'].apply(preprocess_tweet)

# Show cleaned examples
print("\nCleaned Tweets (Training Data):")
print(train_data[['Tweet', 'Clean_Tweet']].head())


# Set a style for prettier plots
sns.set(style="whitegrid")

# Group by Entity and Sentiment, count how many tweets per combination
entity_sentiment_counts = train_data.groupby(['Entity', 'Sentiment']).size().reset_index(name='Count')

# Plot it!
plt.figure(figsize=(14, 6))
sns.barplot(
    data=entity_sentiment_counts,
    x='Entity',
    y='Count',
    hue='Sentiment',
    palette='coolwarm'
)
plt.title('Sentiment Distribution Across Entities')
plt.xlabel('Entity')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=45)
plt.legend(title='Sentiment')
plt.tight_layout()  # optional: adjusts spacing to prevent clipping
plt.savefig("sentiment_analysis_chart.png", dpi=300)  # saves chart
plt.show()


# Count of sentiments per entity
plt.figure(figsize=(12, 6))
sns.countplot(data=train_data, x='Entity', hue='Sentiment', palette='viridis')
plt.title('Sentiment Distribution per Entity (Training Data)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sentiment_per_entity.png", dpi=300)
plt.show()


