import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle

from preprocessing import clean_text

def train_model():
    # Load dataset (use your dataset path)
    df = pd.read_csv('data/spam.csv', encoding='latin-1')
    
    # Keep only required columns
    df = df[['v1', 'v2']]
    df.columns = ['label', 'message']
    
    # Convert labels
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    
    # Clean text
    df['message'] = df['message'].apply(clean_text)
    
    # Features & labels
    X = df['message']
    y = df['label']
    
    # Vectorization
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    # Save model & vectorizer
    pickle.dump(model, open('model.pkl', 'wb'))
    pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
    
    print("Model trained and saved!")

if __name__ == "__main__":
    train_model()
