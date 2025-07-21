from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re
from sklearn.cluster import KMeans


# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small and fast, good enough for clustering

# Assume df['text'] contains one row with a large document — let's split into smaller chunks first


def chunk_text(text, max_words=100):
    words = re.split(r'\s+', text)
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

# Chunking large document
text_chunks = chunk_text(df['text'][0])
chunk_embeddings = model.encode(text_chunks)


num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(chunk_embeddings)

# Attach cluster labels to text chunks
clustered_chunks = [{'text': text_chunks[i], 'cluster': cluster_labels[i]} for i in range(len(text_chunks))]


"""Performing Data Annotation here"""

# For each cluster, pick the first representative
sampled_chunks = []
seen = set()
for chunk in clustered_chunks:
    if chunk['cluster'] not in seen:
        sampled_chunks.append(chunk)
        seen.add(chunk['cluster'])

# Display for annotation
for i, chunk in enumerate(sampled_chunks):
    print(f"\n--- Cluster {chunk['cluster']} ---")
    print(chunk['text'])



"""

Here we will get the sentences that will represent the clusters.

import re
from nltk.tokenize import sent_tokenize


clusters = {
    0: sampled_chunks[0]['text'],
    1: sampled_chunks[1]['text'],
    2: sampled_chunks[2]['text'],
    3: sampled_chunks[3]['text'],
    4: sampled_chunks[0]['text']
}

# Define minimal filters (customize per context)
KEYWORDS = [
    "HIV", "CSR", "environment", "behavioral", "gamification",
    "public health", "youth", "pollution", "regulation", "marketing"
]

def highlight_sentences_from_clusters(clusters, keywords, min_len=50):
    highlights = {}
    for cluster_id, text in clusters.items():
        sentences = sent_tokenize(text)
        filtered = [
            sent.strip() for sent in sentences
            if any(kw.lower() in sent.lower() for kw in keywords) and len(sent) > min_len
        ]
        highlights[cluster_id] = filtered
    return highlights

# Get highlights
highlighted_sentences = highlight_sentences_from_clusters(clusters, KEYWORDS)

# Display results
for cluster_id, sentences in highlighted_sentences.items():
    print(f"\n--- Cluster {cluster_id} ---")
    for sent in sentences:
        print(f"- {sent}")
