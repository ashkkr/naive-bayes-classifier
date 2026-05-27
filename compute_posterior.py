import pandas as pd

categories = ["Business", "Editorial", "Science", "Sports", "World"]

for category in categories:
    df = pd.read_csv(f"{category}_word_frequency.csv")
    df["posterior_probability"] = df["frequency"] / df["frequency"].sum()
    df.to_csv(f"{category}_posterior.csv", index=False)
    print(f"{category}: total_frequency={df['frequency'].sum()}, words={len(df)}")
