from collections import defaultdict, Counter

class NgramModel:
    def __init__(self, n=3):
        self.n = n
        self.model = defaultdict(int)

    def get_ngrams(self, text):
        text = text.lower()
        return [text[i:i+self.n] for i in range(len(text) - self.n + 1)]

    def train(self, queries):
        for query in queries:
            ngrams = self.get_ngrams(query)
            for ng in ngrams:
                self.model[ng] += 1

    def score(self, query, candidate):
        query_ngrams = set(self.get_ngrams(query))
        candidate_ngrams = set(self.get_ngrams(candidate))
        return len(query_ngrams & candidate_ngrams)

    def suggest(self, query, candidates, top_n=5):
        scored = []
        for candidate in candidates:
            score = self.score(query, candidate)
            if score > 0:
                scored.append((candidate, score))
        scored.sort(key=lambda x: -x[1])
        return [c for c, _ in scored[:top_n]]
