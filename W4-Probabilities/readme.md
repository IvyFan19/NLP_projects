Workshop Topic: Next word predictor using a bigram language model

Input: A word

Output : List of words that can follow the input word, and their corresponding probabilities 

Steps to follow:

1) Build the bigram LM:

1.A) Use nltk to compile all the unique bigrams from the corpus you used for the previous assignment.  

1.B) Compute probability of each bigram using MLE ( count(w1 w2) / count(w1) ) 

2) Next word prediction using the above bigram LM:

2.A) Get an input word from user, inpW.

2.B) Use the above bigram LM to find all the bigrams where the input word, inpW, is w1.  Display all possible next words from these bigrams and their corresponding probabilities. 

Example:

Corpus: "I will go to California to meet my friend"

Bigram model : P(will | I) = 1, P(go | will) = 1, P(to | go) = 1, P(California | to) = 0.5, P(to | California) = 1, P(meet | to) = 0.5, P(my | meet) = 1, P(friend | my) = 1

Input string: "to"

Output: 

"Possible next words: California: 0.5, meet: 0.5"