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
