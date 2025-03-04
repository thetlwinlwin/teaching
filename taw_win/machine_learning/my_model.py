from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("taw_win/machine_learning/spam.csv", encoding="latin-1")
df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], inplace=True)

df.rename(columns={"v1": "result", "v2": "emails"}, inplace=True)
df = df.drop_duplicates(keep="first")


# Plotting
plt.figure(figsize=(8, 6))
plt.pie(
    df["result"].value_counts(),
    autopct="%1.1f%%",
    startangle=140,
)
plt.title("Distribution of Spam and Non-Spam Emails")
plt.axis("equal")
plt.show()


# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df["emails"], df["result"], test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF vectorizer and Naive Bayes classifier
spam_filter = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
spam_filter.fit(X_train, y_train)

# Predict on test set
y_pred = spam_filter.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(report)

test_messages = [
    "Congratulations! You've won a free iPhone. Click here to claim now!",
    "Hey, are we still meeting for lunch today?",
    "URGENT: Your bank account is at risk. Verify your details immediately.",
]

predictions = spam_filter.predict(test_messages)

for msg, label in zip(test_messages, predictions):
    print(f"Message: {msg}\nPrediction: {label}\n")
