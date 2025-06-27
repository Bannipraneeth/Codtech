# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Sample Dataset (Ham = not spam, Spam = spam)
data = {
    "label": ["ham", "spam", "ham", "ham", "spam", "spam", "ham", "spam", "ham", "spam"],
    "message": [
        "Hello, how are you?",
        "Congratulations! You've won a free ticket.",
        "Are we meeting tomorrow?",
        "Please call me back.",
        "You’ve been selected for a free prize!",
        "Get cheap meds now!",
        "I’ll be late to the party.",
        "Win money instantly!",
        "Can you send the file?",
        "Claim your free vacation now!"
    ]
}

df = pd.DataFrame(data)

# Step 3: Preprocessing
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
X = df['message']
y = df['label_num']

# Step 4: Vectorize Text
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.3, random_state=0)

# Step 6: Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 7: Predict
y_pred = model.predict(X_test)

# Step 8: Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
