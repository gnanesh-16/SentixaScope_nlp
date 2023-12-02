# -*- coding: utf-8 -*-
"""Emotion-Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GRb6QQWmFxx-biePvtPKPq5rUUBARass
"""

!pip install eli5 lime neattext pandas spacy numpy seaborn altair streamlit

!pip install scikit-learn

import pandas as pd
import numpy as np
import seaborn as sns

#Loading Text Cleaning pkgs
import neattext.functions as nfx

#Load ML Pkgs
#ESTIMATORS
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

#TRANSFORMERS
from sklearn.feature_extraction import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk

import pandas as pd

# Load Dataset and skip lines with parsing errors
df = pd.read_csv("/content/emotion_dataset_2.csv")

df.head()

#Value Counts
df['Emotion'].value_counts()

#plot
sns.countplot(x='Emotion',data=df)

!pip install nfx  # Install the 'nfx' library

#Data CLEANING
import nfx
dir(nfx)

# User handles
df['Clean_Text'] = df['Text'].apply(nfx.remove_userhandles)

# Stopwords
df['Clean_Text'] = df['Clean_Text'].apply(nfx.remove_stopwords)

df

# FEATURES & LABELS
Xfeatures = df['Clean_Text']
ylabels = df['Emotion']

from sklearn.model_selection import train_test_split

# Splitting the data
x_train, x_test, y_train, y_test = train_test_split(Xfeatures, ylabels, test_size=0.3, random_state=42)

# BUILD Pipeline
from sklearn.pipeline import Pipeline

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Creating a Logistic Regression Pipeline
pipe_lr = Pipeline(steps=[('cv', CountVectorizer()), ('lr', LogisticRegression())])

#Check For missing values
import pandas as pd

# Check for missing values in x_train
missing_values = x_train.isnull().sum()
print(missing_values)

# Handlinf Missing Values
# Ensure Data Compatability -> Ensure that the data you're passing to the pipeline is in the appropriate format (byte or unicode string) that the CountVectorizer expects. If needed, preprocess your data to meet this requirement.

"""Assuming x_train is a Pandas Series of text data and y_train is the corresponding labels
# Example:
-> x_train = pd.Series(['text data 1', 'text data 2', 'text data 3', ...])
-> y_train = ...

1. Reshape x_train to make it a 2D array with a single column
2.  Use SimpleImputer to handle missing values
3.  Fit and transform the preprocessed data

-> Assuming x_test is also a Pandas Series, perform similar preprocessing on x_test
1.  Example:
1.x_test = pd.Series(['text data 1', 'text data 2', 'text data 3', ...])


# Create the pipeline with CountVectorizer and LogisticRegression
1.  Fit the pipeline with preprocessed data

2. Flattening the preprocessed data back to 1D array for fitting
3.  Evaluate the model or perform predictions using x_test_preprocessed
    Final __** pipe_lr.predict(x_test_preprocessed.flatten()) **__
"""



from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


# Reshape x_train to make it a 2D array with a single column
x_train_reshaped = x_train.values.reshape(-1, 1)

# Use SimpleImputer to handle missing values
imputer = SimpleImputer(strategy='constant', fill_value='')

# Fit and transform the preprocessed data
x_train_preprocessed = imputer.fit_transform(x_train_reshaped)

# Assuming x_test is also a Pandas Series, perform similar preprocessing on x_test
# Example:
# x_test = pd.Series(['text data 1', 'text data 2', 'text data 3', ...])
x_test_reshaped = x_test.values.reshape(-1, 1)
x_test_preprocessed = imputer.transform(x_test_reshaped)

# Create the pipeline with CountVectorizer and LogisticRegression
pipe_lr = Pipeline(steps=[('cv', CountVectorizer()), ('lr', LogisticRegression())])

# Fit the pipeline with preprocessed data
pipe_lr.fit(x_train_preprocessed.flatten(), y_train)

pipe_lr

# Check Accuracy on the test set
accuracy = pipe_lr.score(x_test_preprocessed.flatten(), y_test)
print("Accuracy on test set:", accuracy)

# Make A Prediction
ex1 = "This book was so interesting it made me happy"

pipe_lr.predict([ex1])

# Prediction Prob
pipe_lr.predict_proba([ex1])

# To Know the classes
pipe_lr.classes_

# Save Model & Pipeline
import joblib
pipeline_file = open("emotion_classifier_pipe_lr_03_june_2021.pkl","wb")
joblib.dump(pipe_lr,pipeline_file)
pipeline_file.close()

! pip install streamlit -q

!wget -q -O - ipv4.icanhazip.com

pip install streamlit pandas numpy joblib altair plotly

! streamlit run app.py & npx localtunnel --port 8501

