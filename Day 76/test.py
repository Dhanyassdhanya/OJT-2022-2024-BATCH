#importing the necessary libraries
from sqlalchemy import create_engine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import mysql.connector

#create an engine of sqlalchemy
def create_sqlalchemy_engine():
    engine = create_engine('mysql+pymysql://root:@localhost/ai_project_db')
    return engine

#create a connection to the database
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ai_project_db"
    )
    return connection

#setup the database as well as query over here
def setup_database():
    connection = create_connection()
    cursor = connection.cursor()
    # create the query  for r if the database is not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS ai_project_db")
    #use database
    cursor.execute("USE ai_project_db")
    # create the table if not exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS
                   dataset(
                   id INT AUTO_INCREMENT
                   PRIMARY KEY,
                   feature1 FLOAT,
                   feature2 FLOAT,
                   label INT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS
                   predictions(
                   id INT,
                   prediction INT)""")
    connection.commit()
    cursor.close()
    connection.close()

#fetch data
def fetch_data():
    engine = create_sqlalchemy_engine()
    query = "SELECT * FROM dataset"
    df = pd.read_sql(query, engine)
    return df

def train_model(df):
    x = df[['feature1', 'feature2']]
    y = df['label']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    return prediction

#store the predictions in mysql db
def store_predictions(predictions):
    connection = create_connection()
    cursor = connection.cursor()
    data = [(i+1, int(pred)) for i, pred in enumerate(predictions)]
    cursor.executemany("INSERT INTO predictions(id, prediction) VALUES(%s, %s)", data)
    connection.commit()
    cursor.close()
    connection.close()

def insert_sample_data():
    data = [
        (1.5, 2.5, 0),
        (2.5, 4.5, 1),
        (2.0, 3.1, 1),
        (1.8, 2.9, 0),
        (1.1, 2.1, 1),
    ]
    connection = create_connection()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO dataset(feature1, feature2, label) VALUES(%s, %s, %s)", data)
    connection.commit()
    cursor.close()
    connection.close()

#create the main class to initiate the function
def main():
    setup_database()
    connection = create_connection()
    insert_sample_data()
    df = fetch_data()
    predictions = train_model(df)
    print("predictions:", predictions)
    store_predictions(predictions)

if __name__ == "__main__":
    main()