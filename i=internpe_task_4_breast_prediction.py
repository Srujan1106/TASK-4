# -*- coding: utf-8 -*-
"""i=Internpe Task 4 Breast Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NNGZYdBrNKmO4kHqaVETGsrGHVsB22b8
"""

import pandas as pd

df=pd.read_csv('/content/data.csv')

df.head(11)

df.info()

df.isna().sum()

df.describe()

df = df.dropna(axis=1)

df.head(11)

df.shape

df['diagnosis'].value_counts()

import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='diagnosis', data=df)
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.title('Diagnosis Count Plot')
plt.show()

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df.iloc[:, 1]=lb.fit_transform(df.iloc[:, 1].values)

df.head(11)

df['diagnosis'].value_counts()

df.corr()

import matplotlib.pyplot as plt

plt.figure(figsize=(25,25))

sns.heatmap(df.iloc[:, 1:10].corr(), annot=True)

sns.pairplot(df.iloc[:, 1:6], hue="diagnosis")

X=df.iloc[:, 2:32].values
X

y = df.iloc[:, 1].values
y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
from sklearn.preprocessing import StandardScaler
st  = StandardScaler()
X_train  = st.fit_transform(X_train)
X_test  = st.fit_transform(X_test)

X_train.shape

y_train.shape

from sklearn.linear_model import LogisticRegression, LinearRegression
log = LogisticRegression()
log.fit(X_train, y_train)
log.score(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report
accuracy_score(y_test, log.predict(X_test))
print(classification_report(y_test, log.predict(X_test)))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from ipywidgets import widgets
from IPython.display import display

class BreastCancerDetectionApp:
    def __init__(self):
        # Load breast cancer dataset
        data = load_breast_cancer()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )

        # Create and train the model
        self.model = RandomForestClassifier(random_state=42)
        self.model.fit(self.X_train, self.y_train)

        # Create GUI components
        self.label = widgets.Label(value="Enter features for prediction:")
        self.features_entry = widgets.Text()
        self.predict_button = widgets.Button(description="Predict")
        self.result_label = widgets.Label(value="")

        # Define event handlers
        self.predict_button.on_click(self.predict)

        # Display GUI components
        display(self.label, self.features_entry, self.predict_button, self.result_label)

    def predict(self, button):
        # Get input features from the user
        input_features = [float(x) for x in self.features_entry.value.split(",")]

        # Standardize input features
        scaler = StandardScaler()
        scaler.fit(self.X_train)
        input_features_std = scaler.transform([input_features])

        # Make prediction
        prediction = self.model.predict(input_features_std)

        # Display the result
        result_text = "Malignant" if prediction[0] == 0 else "Benign"
        self.result_label.value = f"Prediction: {result_text}"

# Create the app
app = BreastCancerDetectionApp()

