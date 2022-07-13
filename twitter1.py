import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import re
import nltk
import nltk

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/twitter.csv")
print(data.head())