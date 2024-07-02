import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import sklearn as sklearn
df=pd.read_csv("data.csv")

# Specify the row numbers (index) of the first and last columns you want to include
first_column_index = 2  # Replace with the actual index of the first column
last_column_index = 32  # Replace with the actual index of the last column

# Assuming 'data' is your DataFrame
column_number_to_drop = 32 # Replace with the actual column number you want to drop

# Get the column name by column number
column_name_to_drop = df.columns[column_number_to_drop]

# Drop the column by name
df.drop(column_name_to_drop, axis=1, inplace=True)
# Extract feature columns using iloc
x = df.iloc[:, first_column_index:last_column_index + 1]

# Assuming 'target_column' is the target variable
target_column = 'diagnosis'

# Extract the target variable
y = df[target_column]
from sklearn.model_selection import train_test_split

# Specify the test size (e.g., 0.2 for 80% train, 20% test)
test_size = 0.2

# Use train_test_split to split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Assuming X_train and X_test are your feature sets
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Adjusting the Logistic Regression model
model = LogisticRegression(max_iter=1000, solver='lbfgs')
model.fit(x_train_scaled, y_train)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
y_pred = model.predict(x_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
