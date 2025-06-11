from sklearn.feature_extraction.text import TfidfVectorizer

TOP_K = 50

async def compute_tfidf_from_text(text: str) -> list[dict]:
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([text])
    tfidf_scores = dict(zip(vectorizer.get_feature_names_out(), X.toarray()[0]))
    sorted_words = sorted(tfidf_scores.items(), key=lambda x: -x[1])[:TOP_K]

    # Convert to list of dictionaries
    result = [{"term": term, "score": float(score)} for term, score in sorted_words]
    return result




async def compute_tfidf_from_text_for_statistics(texts: list[str]) -> list[dict]:
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)  # multiple documents
    tfidf_matrix = X.toarray()
    feature_names = vectorizer.get_feature_names_out()

    # Aggregate top terms across all documents
    term_scores = {}
    for doc_vec in tfidf_matrix:
        for i, score in enumerate(doc_vec):
            term = feature_names[i]
            term_scores[term] = term_scores.get(term, 0) + score

    sorted_terms = sorted(term_scores.items(), key=lambda x: -x[1])[:TOP_K]
    return [{"term": term, "score": round(score, 5)} for term, score in sorted_terms]
