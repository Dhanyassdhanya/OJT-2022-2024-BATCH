#  Load the dataset from a CSV file named sample_dataset.csv into a Pandas DataFrame. Display the first few rows of the dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import GridSearchCV

df = pd.read_csv("sepal_dataset.csv")

# Display the first few rows of the dataset.
print(df.head())
# Generate summary statistics for this dataset. What are the mean and standard deviation of the Sepal Length
# Generating summary statistics
summary_stats = df.describe()

# Calculating mean and standard deviation for Sepal Length
mean_sepal_length = df['Sepal Length (cm)'].mean()
std_sepal_length = df['Sepal Length (cm)'].std()

summary_stats, mean_sepal_length, std_sepal_length
# Checking for missing values
missing_values = df.isnull().sum()

from sklearn.model_selection import train_test_split

# Features and target variable
X = df.drop(columns=['Species'])
y = df['Species']

# Splitting the dataset (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

X_train.shape, X_test.shape, y_train.shape, y_test.shape
from sklearn.tree import DecisionTreeClassifier

# Training a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Plotting the decision tree
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=['FlowerA', 'FlowerB', 'FlowerC'], filled=True)
plt.show()
from sklearn.metrics import accuracy_score

# Making predictions on the testing data
y_pred = clf.predict(X_test)

# Computing the accuracy
accuracy = accuracy_score(y_test, y_pred)


from sklearn.metrics import classification_report, confusion_matrix

# Generating the classification report
class_report = classification_report(y_test, y_pred, target_names=['FlowerA', 'FlowerB', 'FlowerC'])

# Generating the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)