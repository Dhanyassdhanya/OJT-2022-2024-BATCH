import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Create sample data
reviews = [
    "I love the movie, it was good",
    "The movie was boring",
    "Excellent movie, actors did well",
    "It was a normal movie, nothing special"
]

# Labels: Positive = 1, Negative = 0, Neutral = 2
labels = [1, 0, 1, 2]

# Create vectorization for the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)
y = np.array(labels)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LogisticRegression(max_iter=1000)  # Added max_iter to ensure convergence
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Create a sample review for prediction
new_review = ["I really enjoyed the movie"]
new_review_transformed = vectorizer.transform(new_review)
new_review_prediction = model.predict(new_review_transformed)

print(f"Predicted label for the new review: {new_review_prediction[0]}")


# In[ ]:




