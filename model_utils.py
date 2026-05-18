import joblib

model = joblib.load("saved_model/classifier.pkl")
embedder = joblib.load("saved_model/embedder.pkl")


def predict_risk(text):

    vec = embedder.encode(
        [text],
        normalize_embeddings=True
    )

    score = model.predict_proba(vec)[0][1]

    return float(score)