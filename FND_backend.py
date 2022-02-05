import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import joblib
# import nltk

# nltk.download('stopwords')

model = joblib.load('news_model')
vectorizer = joblib.load('vectorizer.pkl')
news_dataset2 = pd.read_csv('newtest.csv')

# To check dimensions of dataset (remove comments)
# news_dataset2.shape

# To print the first 5 rows of the train dataframe (remove comments)
# news_dataset2.head()

# Counting the number of missing values in the dataset
# news_dataset2.isnull().sum()

# replacing the null values with empty string
news_dataset2 = news_dataset2.fillna('')

# merging the author name and news title
news_dataset2['content'] = news_dataset2['author'] + ' ' + news_dataset2['title']

# To check dataset content (remove comments)
# print(news_dataset2['content'])

port_stem = PorterStemmer()


def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content


news_dataset2['content'] = news_dataset2['content'].apply(stemming)
# print(news_dataset2['content'])

X_test = news_dataset2['content'].values
X_test = vectorizer.transform(X_test)
# print(X_test)

X_test_prediction = model.predict(X_test)
print(X_test_prediction)
