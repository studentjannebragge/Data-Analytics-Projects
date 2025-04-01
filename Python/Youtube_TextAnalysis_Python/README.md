# YouTube Text Analysis

This project focuses on analyzing YouTube comments to extract meaningful insights using Python. The analysis includes sentiment analysis, emoji frequency, and relationships between various metrics like views, likes, and comments.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction
YouTube is one of the largest platforms for user-generated content, and analyzing its comments can provide valuable insights into user sentiment, engagement, and trends. This project uses Python to process and analyze YouTube comments, focusing on:
- Sentiment analysis (positive, negative, neutral)
- Emoji frequency analysis
- Relationships between views, likes, and comments

## Features
- **Sentiment Analysis**: Classifies comments as positive, negative, or neutral.
- **Emoji Analysis**: Extracts and visualizes the most frequently used emojis.
- **EDA (Exploratory Data Analysis)**: Analyzes relationships between metrics like views, likes, and comments.
- **Database Integration**: Stores processed data in an SQLite database for efficient querying.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `matplotlib` and `seaborn` for data visualization
  - `plotly` for interactive visualizations
  - `sqlite3` and `sqlalchemy` for database management
  - `textblob` for sentiment analysis
  - `emoji` for emoji extraction
- **Database**: SQLite

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/YouTube_TextAnalysis.git
   cd YouTube_TextAnalysis
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place your YouTube comments dataset (e.g., `UScomments.csv`) in the appropriate directory.

## Usage
1. Run the Jupyter Notebook:
   ```bash
   jupyter notebook youtube_analysis.ipynb
   ```

2. Follow the steps in the notebook to:
   - Load and clean the data.
   - Perform sentiment analysis.
   - Visualize emoji frequency and other metrics.
   - Store and query data using SQLite.

3. Export results:
   - Processed data is saved in the `export_data/` directory as CSV and SQLite files.

## Results
- **Sentiment Analysis**: Majority of users express positive sentiments, with frequent use of emojis like ❤️, 😂, and 😍.
- **Emoji Frequency**: The most common emojis reflect user engagement and sentiment.
- **EDA**: Strong correlation observed between likes and views.


---

Feel free to contribute to this project by submitting issues or pull requests. Happy analyzing!