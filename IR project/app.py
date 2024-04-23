import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Indexer:
    def __init__(self):
        self.documents = []
        self.index = None
        self.vectorizer = TfidfVectorizer()

    def index_documents(self, documents):
        self.documents = documents
        self.index = self.vectorizer.fit_transform(documents)

    def save_index(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump((self.vectorizer, self.index), f)

    def load_index(self, filepath):
        with open(filepath, 'rb') as f:
            self.vectorizer, self.index = pickle.load(f)

    def search(self, query, top_k=5):
        if self.index is None or self.vectorizer is None:
            raise ValueError("Index is not initialized. Please index documents first.")

        # Transform query into TF-IDF representation
        query_vector = self.vectorizer.transform([query])

        # Calculate cosine similarity between query and documents
        similarities = cosine_similarity(query_vector, self.index)

        # Return top-K ranked results based on similarity scores
        ranked_results = [(score, self.documents[i]) for i, score in enumerate(similarities[0])]
        ranked_results.sort(reverse=True)
        return ranked_results[:top_k]

from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
indexer = Indexer()

# Load documents
documents = []
for filename in ["quotes-historical-fiction_4.html", "quotes-mystery_3.html", "quotes-travel_2.html"]:
    with open(filename, 'r', encoding='utf-8') as file:
        documents.append(file.read())

# Index documents
indexer.index_documents(documents)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Empty query'}), 400

    top_k = data.get('top_k', 5)

    # Perform search
    results = indexer.search(query, top_k=top_k)

    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(debug=True)
