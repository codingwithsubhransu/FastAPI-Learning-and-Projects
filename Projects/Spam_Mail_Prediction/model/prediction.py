import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

MODEL_VERSION = '1.0.0'

with open('model/spam_mail_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/feature_extraction.pkl', 'rb') as f:
    feature_extraction = pickle.load(f)


def predict_output(user_input: list) -> int:
    input_mail_feature = feature_extraction.transform(user_input)
    predicted_class = "Spam" if model.predict(input_mail_feature)[0] == 0 else "Ham"
    probabilities = model.predict_proba(input_mail_feature)[0]
    confidence = max(probabilities)
    return {
        "predicted_class": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": {
            "spam_confidence": round(probabilities[0], 4),
            "Ham_confidence": round(probabilities[1], 4)
        }
    }