
## NLTK-chatbox
1. Install NLTK: https://www.nltk.org/

2. Develop a chatbot that provides simple emotional support for students by being a good "listener". For example, when the user says "The finals week has been tough", the chatbot could respond "I hear you. Finals week is tough for many. Do you want to tell me more?"  

Use the "nltk.chat.eliza" module for this chatbot.

You will need to know how to use regex in NLTK for this : https://www.nltk.org/_modules/nltk/tokenize/regexp.html

--------------------------

## Use Levenshtein's minimum edit distance to find the closest words to the user input

Workshop Topic: Use Levenshtein's minimum edit distance to find the closest words to the user input

Write a program that uses nltk library:

Input argument: A string of characters (that is, it doesn't have to be a complete word)

Output: 

	If the input string exists in the vocabulary then your program should output "[XYZ] is a complete and correct word in English."

	If the input string doesn't exist in the vocabulary then your program should output the 5 closest words to it as measured by Levenshtein distance.

Steps to follow:

1) Build a vocabulary (set of all unique words) using any English corpus from nltk. The input string will be searched in this vocabulary.

2) Find the no. of occurrences (frequency) of each unique word in the chosen corpus.  Also, find the total number of words in the chosen corpus (N).

3) Find the relative frequency of each word x where relative frequency of x = frequency of x / N. This relative frequency can be interpreted as the probability of each word in the corpus.  

4) For every input string:

4.a) If the input string XYZ exists in your vocabulary, return "XYZ is a complete and correct word in English."

4.b) If the input string doesn't exist in your vocabulary, perform the below steps:

4.b.i) Calculate the similarity between each word in the vocabulary and the input string using Levenshtein distance. (Use any open-source python library for calculating Levenshtein distance.) 

4.b.ii) Output the closest top 5 words as per Levenshtein distance to the input string. Also, output the probability for each of the 5 words.

-------------------------------

## Next word predictor using a bigram language model

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

-----------------------------
### TEXT CLASSIFICATION USING NAIVE BAYES

1) Create a toy labeled dataset.  (Use any data structure in python to store this data). This dataset should have 10-15 sentences with a class label associated with each datapoint. There should be at least 2 classes (e.g. spam vs ham OR positive vs negative)

2) Calculate the prior probabilities. 

3) Calculate the conditional probabilities of each word (with respect to both the categories) in the dataset. 

4) Take a sentence as input from the user. 

5) Using the probabilities calculated before and Naive Bayes classification, predict the class of the input sentence. (Calculate the probability of the input sentence being in different classes. The class having the highest probability will be the output class.)

Note : Refer to the 9th slide of 03/02 slide deck for more details.



Example dataset
Text	Class
You know nothing Jon Snow 
0
Yer a wizard Harry
1
You are going to die tomorrow, Lord Bolton. Sleep well	0
Training for the ballet, Potter?	1
Tell Cersie,I want her to know it was me	0
Fawkes is a phoenix, Harry.	1
Winter is coming	0
Don’t let the muggles get you down	1

Input text:

Of course, it is happening inside your head, Harry

Output 

Category 1

Explanation:

Class 0 - Dialogues from Game of Thrones

Class  1 - Dialogues from Harry Potter

Input text : Dialogue from Harry Potter. Thus, it has to be classified as 1.

