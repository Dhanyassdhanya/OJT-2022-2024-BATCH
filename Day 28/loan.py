# Packages that need to be imported for this loan repayment prediction.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,recall_score,precision_score
from sklearn.model_selection import GridSearchCV

# loan the dataset loan_data.csv
data = pd.read_csv('loan_data.csv')

# Selected the features which need to be used in the case
x = data[['loan_amount','interest_rate','term','income','credit_score',
          'age','employment_length']]
y = data['loan_repaid']

# Split train_tests
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,random_state=42)

# Initiate a model
model = DecisionTreeClassifier(random_state=42)

# train the model
model.fit(x_train,y_train)

# Make a prediction 
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print(f"accuracy: {accuracy:.2f}")
print("Classifiication_report :")
print(classification_report(y_test,y_pred))

# Precision
precision = precision_score(y_test, y_pred)
print("Precision: ", accuracy_score(y_test, y_pred))

# recall
recall = recall_score(y_test, y_pred)
print("Recall: ", recall)

# F1Score
f1 = 2 * (precision * recall) / (precision + recall)
print("F1 Score: ", f1)


