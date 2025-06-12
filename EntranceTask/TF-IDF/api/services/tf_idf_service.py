from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from typing import List, Dict


TOP_K = 50


async def compute_tfidf_from_text(text: str) -> List[Dict]:
    """
    Computes TF-IDF statistics for a single document.
    Uses raw term frequency (TF = term count / total terms) and raw IDF (no normalization).
    """
    vectorizer = TfidfVectorizer(stop_words="english", norm=None)
    X = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    idf_values = vectorizer.idf_

    # Count raw term frequencies (after tokenization from TfidfVectorizer)
    tokenized = vectorizer.build_analyzer()(text)
    term_counts = Counter(tokenized)
    total_terms = sum(term_counts.values())

    result = []
    for idx, term in enumerate(feature_names):
        tf = term_counts[term] / total_terms if total_terms else 0.0
        idf = idf_values[idx]
        tfidf_score = tf * idf
        result.append({
            "term": term,
            "tf": round(tf, 6),
            "idf": round(idf, 6),
            "score": round(tfidf_score, 6)
        })

    sorted_result = sorted(result, key=lambda x: -x["score"])[:TOP_K]
    return sorted_result


async def compute_tfidf_from_text_for_statistics(texts: List[str]) -> List[Dict]:
    """
    Computes aggregated TF-IDF statistics across multiple documents.
    This function sums TF and score values per term across documents.
    """
    vectorizer = TfidfVectorizer(stop_words="english", norm=None)
    X = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    idf_values = vectorizer.idf_
    tfidf_matrix = X.toarray()

    # Get raw term counts per document
    all_term_data = []
    for text in texts:
        tokens = vectorizer.build_analyzer()(text)
        counts = Counter(tokens)
        total = sum(counts.values())
        tf_dict = {term: count / total for term, count in counts.items()}
        all_term_data.append(tf_dict)

    term_data = {}

    for doc_index, row in enumerate(tfidf_matrix):
        tf_dict = all_term_data[doc_index]
        for i, tfidf_score in enumerate(row):
            if tfidf_score == 0:
                continue
            term = feature_names[i]
            idf = idf_values[i]
            tf = tf_dict.get(term, 0.0)
            if term not in term_data:
                term_data[term] = {"tf": 0.0, "score": 0.0, "idf": idf}
            term_data[term]["tf"] += tf
            term_data[term]["score"] += tf * idf

    result = []
    for term, values in term_data.items():
        result.append({
            "term": term,
            "tf": round(values["tf"], 6),
            "idf": round(values["idf"], 6),
            "score": round(values["score"], 6)
        })

    sorted_result = sorted(result, key=lambda x: -x["score"])[:TOP_K]
    return sorted_result
