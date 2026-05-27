import re
import pandas as pd

PRIORS = {
    "World":     0.2528,
    "Business":  0.2111,
    "Sports":    0.3333,
    "Editorial": 0.1389,
    "Science":   0.0639,
}

posteriors = {}
total_freqs = {}
for category in PRIORS:
    df = pd.read_csv(f"{category}_posterior.csv")
    posteriors[category] = dict(zip(df["word"], df["posterior_probability"]))
    total_freqs[category] = df["frequency"].sum()

def clean(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"[^a-z\s]", "", sentence)
    return sentence.split()

def classify(sentence):
    words = clean(sentence)
    scores = {}
    for category, prior in PRIORS.items():
        score = prior
        for word in words:
            if word in posteriors[category]:
                p_word = posteriors[category][word]
            else:
                p_word = 0.5 / total_freqs[category]
            score *= p_word
        scores[category] = score

    best = max(scores, key=scores.get)
    return best, scores

sentence = input("Enter a newspaper heading: ")
predicted, scores = classify(sentence)

print(f"\nPredicted category: {predicted}")
print("\nScores (all categories):")
for cat, score in sorted(scores.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {score:.6e}")
