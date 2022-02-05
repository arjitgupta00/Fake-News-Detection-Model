import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import nltk
nltk.download('stopwords')
# Printing the stopwords in English

# print(stopwords.words('english'))

# Loading the dataset to a pandas DataFrame
news_dataset = pd.read_csv('C:\\Users\\Arjit\\Desktop\\train.csv')

# news_dataset.shape
# print the first 5 rows of the dataframe
news_dataset.head()

# counting the number of missing values in the dataset
news_dataset.isnull().sum()

# replacing the null values with empty string
news_dataset = news_dataset.fillna('')

# merging the author name and news title
news_dataset['content'] = news_dataset['author']+' '+news_dataset['title']

# separating the data & label
X = news_dataset.drop(columns='label', axis=1)
Y = news_dataset['label']

port_stem = PorterStemmer()


def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content


news_dataset['content'] = news_dataset['content'].apply(stemming)

# noinspection PyRedeclaration
X = news_dataset['content'].values
# noinspection PyRedeclaration
Y = news_dataset['label'].values

# converting the textual data to numerical data
vectorizer = TfidfVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)

model = LogisticRegression()
model = model.fit(X, Y)
joblib.dump(model, 'news_model')
joblib.dump(vectorizer, 'vectorizer.pkl')
