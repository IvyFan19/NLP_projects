TEXT CLASSIFICATION USING NAIVE BAYES

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

