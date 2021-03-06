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