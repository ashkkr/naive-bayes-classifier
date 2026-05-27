This is a naive bayes classifier for newspaper headlines.

What is naive bayes?
Naive bayes is a simplified application of bayes rule that uses conditional independence.
Posterior probability distribution of a text over categories is calculated by multiplying prior probability of that category with posterior probabilities of each word, given the category.

How was this model trained?
We formed this model from newspaper articles of TheHindu newspaper. For simplicity, we considered only categories - Science, World, Business, Sports and Editorial. And, we only used articles of 5 days. We used claude agent to scrape articles and note down word frequencies in category-wise files. ( See Science_posterior.csv). 

How was posterior probability of each word calculated?
Posterior probability of a word is probability of seeing that word given a category. For example, P(HasWord = "cricket" | Category = Business). 
Hence, posterior probability is calculated simply by dividing frequency of a word occurence withing a category divided by total frequencies of that category. 
This is implemented in the file compute_posterior.py

How was sentence classified? 
See classify.py. Now, once we receive a sentence. We can assume all words to be conditionally independent to apply naive bayes. 
Then, we fetch and product posterior probabilities of each word and multiply the result with prior probability of that category. This gives us a probability distribution across categories for each sentence. We can chose the category with highest 'score' to classify the sentence. 
Caveat: Sometimes, we might see an entirely new word in a category that our model has not seen. We cannot assign it a probability of zero, because that would remove that category from consideration. Hence, we assume all words occur with frequence 0.5 if no frequency if found. 

Testing and Results
There on, we got 50 random headlines across categories from the same newspaper and used our Naive Bayes model to classify them. Results showed an accuracy of 64%. 

Further improvements
This model can be further improved in any of the following ways 
    From word frequencies, common words like the,has,had can be removed as they tell no information about category
    Words can be standardised like talk,talking,talks should be counted as one words
    Assumed frequency of words that have not been seen before can be reconsidered, as our approach is not reasonable

