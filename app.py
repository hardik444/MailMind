from src.predict import predict_email

print("📧 MailMind - Spam Detection System")
print("-----------------------------------")

while True:
    email = input("\nEnter email text (or type 'exit' to quit): ")
    
    if email.lower() == 'exit':
        break
    
    result = predict_email(email)
    print(f"Prediction: {result}")
