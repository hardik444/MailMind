import pickle
from preprocessing import clean_text

# Load model & vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predict_email(text):
    text = clean_text(text)
    text_vector = vectorizer.transform([text])
    
    prediction = model.predict(text_vector)[0]
    
    return "Spam" if prediction == 1 else "Not Spam"
