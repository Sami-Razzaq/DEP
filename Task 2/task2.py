# Implement a spam email classifier using machine learning algorithms like Naive Bayes or Support Vector Machines.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("./emails.csv")

# Get Features and Labels from dataset
# Labels = either  given email is spam or not
labels = data['Prediction']
features = data.drop(['Email No.', 'Prediction'], axis=1)

labels = np.array(labels)
features = np.array(features)

# Divide Data into Train Test - 20% Test
X_train, X_test, y_train, y_test=train_test_split(features, labels, test_size=0.2)


# Training  
nb = MultinomialNB()
nb.fit(X_train, y_train)