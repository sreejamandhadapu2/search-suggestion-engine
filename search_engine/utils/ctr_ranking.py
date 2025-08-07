from collections import defaultdict

class CTRRanker:
    def __init__(self):
        self.clicks = defaultdict(int)
        self.impressions = defaultdict(int)

    def update(self, query, clicked):
        self.impressions[query] += 1
        if clicked:
            self.clicks[query] += 1

    def rank(self, suggestions):
        def ctr(query):
            imp = self.impressions[query]
            clk = self.clicks[query]
            return clk / imp if imp > 0 else 0
        return sorted(suggestions, key=ctr, reverse=True)
