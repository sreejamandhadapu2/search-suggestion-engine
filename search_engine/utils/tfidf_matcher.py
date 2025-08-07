from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfidfMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.corpus = []

    def train(self, corpus):
        self.corpus = corpus
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)

    def suggest(self, query, top_n=5):
        if self.tfidf_matrix is None:
            return []

        query_vec = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = similarity_scores.argsort()[::-1][:top_n]
        return [self.corpus[i] for i in top_indices]
