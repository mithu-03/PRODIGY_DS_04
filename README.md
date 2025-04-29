# Twitter Sentiment Analysis - Entity-wise Visualization

## Project Overview
This project focuses on analyzing sentiment patterns in Twitter data using the `twitter_training.csv` and `twitter_validation.csv` datasets.  
The main goal is to clean the raw tweets, explore the distribution of sentiments, and visualize sentiment trends across different entities (e.g., companies, topics, etc.).

---

## Project Files
```
/PRODIGY_DS_04
├── twitter_training.csv                    # Training dataset
├── twitter_validation.csv                  # Validation dataset
├── sentiment.py                            # Python script for EDA and preprocessing
├── sentiment_distribution.png              # Bar chart showing overall sentiment distribution
├── sentiment_analysis_chart.png            # Sentiment grouped by entities
├── sentiment_per_entity.png                # Countplot of sentiment per entity
└── README.md                               # This file
```

---

## Data Preprocessing Steps
- Loaded datasets with custom column names: ID, Entity, Sentiment, Tweet
- Dropped tweets with missing content
- Preprocessed tweets by:
  - Lowercasing
  - Removing URLs, mentions, hashtags, and non-alphabetic characters
  - Removing stopwords using NLTK
- Created a new `Clean_Tweet` column for analysis

---

## Visualizations
- **Overall Sentiment Distribution** → Total positive, neutral, and negative tweets
- **Sentiment by Entity** → Grouped bar plot comparing sentiment counts across topics
- **Entity-Wise Countplot** → Additional plot to compare sentiment variations for each entity

---

## Libraries Used
- pandas
- matplotlib
- seaborn
- re
- nltk (for stopwords)

---

## Key Insights
- Sentiments are fairly balanced across entities, with some skewed trends for specific topics.
- Preprocessing significantly reduces noise in tweets, enabling better insights.
- Visualizations reveal public perception of various entities on Twitter.

---

## How to Run
1. Ensure Python is installed
2. Install required libraries:
    ```
    pip install pandas matplotlib seaborn nltk
    ```
3. Run the script:
    ```
    python sentiment.py
    ```
4. The following image files will be saved:
   - `sentiment_distribution.png`
   - `sentiment_analysis_chart.png`
   - `sentiment_per_entity.png`

---

## Credits
This project was completed as part of the **Data Science Internship** at **Prodigy Infotech**.

Created by **Mithra**  
_B.Tech Artificial Intelligence & Data Science Student_

---

