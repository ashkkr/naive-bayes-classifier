# Naive Bayes Newspaper Headline Classifier

A Naive Bayes classifier for newspaper headlines, trained on articles from TheHindu across five categories: **Science**, **World**, **Business**, **Sports**, and **Editorial**.

## What is Naive Bayes?

Naive Bayes is a simplified application of Bayes' rule that assumes conditional independence between features. The posterior probability of a text belonging to a category is calculated by multiplying the prior probability of that category with the posterior probabilities of each word given the category.

## How was this model trained?

The model was built from TheHindu newspaper articles over 5 days. A Claude agent was used to scrape articles and record word frequencies into category-wise files (e.g. `Science_posterior.csv`).

## How was posterior probability of each word calculated?

The posterior probability of a word is `P(HasWord = w | Category = C)` — the probability of seeing that word given a category. It is calculated by dividing the frequency of a word within a category by the total word frequency for that category.

See [`compute_posterior.py`](compute_posterior.py) for the implementation.

## How is a sentence classified?

See [`classify.py`](classify.py). Given a sentence, all words are assumed to be conditionally independent (the Naive Bayes assumption). The posterior probabilities of each word are multiplied together and then multiplied by the prior probability of the category. The category with the highest score is selected.

**Caveat:** For words the model has never seen in a category, a frequency of `0.5` is assumed to avoid zeroing out that category from consideration.

## Results

50 random headlines across categories were classified using the model. Results showed an **accuracy of 64%**. See [`headlines_by_category.csv`](headlines_by_category.csv) for the full list of headlines, their actual categories, and predicted categories.

## Further Improvements

- Remove common stop words (e.g. *the*, *has*, *had*) that carry no category information
- Standardise word forms — *talk*, *talking*, *talks* should be counted as one word (stemming/lemmatisation)
- Reconsider the assumed frequency of `0.5` for unseen words — a more principled smoothing approach (e.g. Laplace smoothing) could improve accuracy
