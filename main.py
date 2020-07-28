from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import svm

class CustomSVC(svm.SVC):
    
    def __init__(self,vectorizer='Tfidf',  C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None):
      super().__init__(C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
      if vectorizer = 'Count':
        self.vectorizer = CountVectorizer()
      else:
        self.vectorizer = TfidfVectorizer()

    def fit(self, x, y):
      x_vectors = self.vectorizer.fit_transform(x)
      super().fit(x_vectors, y)

    def predict(self, x):
      x_vectors = self.vectorizer.transform(x)
      return super().predict(x_vectors)
