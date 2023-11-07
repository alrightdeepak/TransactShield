import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# step: represents a unit of time where 1 step equals 1 hour
# type: type of online transaction
# amount: the amount of the transaction
# nameOrig: customer starting the transaction
# oldbalanceOrg: balance before the transaction
# newbalanceOrig: balance after the transaction
# nameDest: recipient of the transaction
# oldbalanceDest: initial balance of recipient before the transaction
# newbalanceDest: the new balance of recipient after the transaction
# isFraud: fraud transaction

data = pd.read_csv(r"C:\Users\UseR\ocv project\project3\credit.csv")
print('\n',"DATA EXPLORATION \n")
print(data.head())
print('\n',"Checking if the data has any Null values: ")
print(data.isnull().sum())

# Exploring transaction type
print('\n',"Type of transactions mentioned in the data: ")
print(data.type.value_counts())

#pi chart of the data
type = data["type"].value_counts()
transactions = type.index
quantity = type.values

figure = px.pie(data, 
             values=quantity, 
             names=transactions,hole = 0.5, 
             title="Distribution of Transaction Type")
figure.show()

# Checking correlation
print('\n',"Correlation of data: ")
correlation = data.corr(numeric_only=True)
print(correlation["isFraud"].sort_values(ascending=False))

#data manipulation
print('\n',"Changing the data in numeric form: ")
data["type"] = data["type"].map({"CASH_OUT": 1, "PAYMENT": 2, 
                                 "CASH_IN": 3, "TRANSFER": 4,
                                 "DEBIT": 5})
data["isFraud"] = data["isFraud"].map({0: "No Fraud", 1: "Fraud"})

# splitting the data in train and test data and training the model

x = np.array(data[["type", "amount", "oldbalanceOrg", "newbalanceOrig"]])
y = np.array(data[["isFraud"]])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.10, random_state=42)
model = DecisionTreeClassifier()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

# prediction
#features = [type, amount, oldbalanceOrg, newbalanceOrig]
print('\n',"Entering a transaction and predicting whether it is fraud or not: ")
features = np.array([[4, 9000.60, 12000, 0.0]])
print(model.predict(features))