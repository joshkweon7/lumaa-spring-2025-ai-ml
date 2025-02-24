import pandas as pd 
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#1. function to load in database of books and their summaries 
def load_data(file):
    df = pd.read_csv(file)
    return df

#2. function to convert data set into vectors using tf-idf
def preprocess(data, text_column):
    vectorizer = TfidfVectorizer(stop_words='english') 
    tfidfmatrix = vectorizer.fit_transform(data[text_column]) # converts dataset into tf-idf vectors 
    return tfidfmatrix, vectorizer

#3. calculate similarity scores 
def get_similarity(input, tfidf_matrix, vectorizer): 
    user_tfidf = vectorizer.transform([input]) # transforms the users input into tf-idf vectors 
    similarity_score = cosine_similarity(user_tfidf, tfidf_matrix).flatten() # computes the similarity score between the user and dataset vectors
    return similarity_score 

#4. list recommendations based on similarity scores
def recommend_book(input, data, text_column = 'summaries', top_n = 5):
    tfidf_matrix, vectorizer = preprocess(data, text_column)
    similarity_score = get_similarity(input, tfidf_matrix, vectorizer) # calls functions above
    data['similarity'] = similarity_score # adds new column for similarity scores
    recommendations = data.sort_values(by = 'similarity', ascending = False).head(top_n) # sorts by highest similarity 
    recommendations = recommendations[['book_name', 'similarity']].reset_index(drop=True)
    recommendations.index = recommendations.index + 1 
    recommendations.index.name = "Rank" 
    return recommendations

if __name__ == "__main__":
    dataset = "booksummary.csv"
    data_file = load_data(dataset)
    user_query = input("Enter your book preference: ")
    results = recommend_book(user_query, data_file)
    print("Top 5 Recommendations: ")
    print(results)