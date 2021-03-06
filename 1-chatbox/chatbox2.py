import nltk
from nltk.chat.util import Chat, reflections
from nltk.tokenize import RegexpTokenizer

# Get whole pairs from nltk.chat.eliza.pairs
pairs = nltk.chat.eliza.pairs

pairs = (("the finals week is (.*)" , ("Em.. I hear you. Finals week is %1 for many. Do you want to tell me more?",)),) + pairs
pairs = (("(.*) homework is (.*)", ("I agree! %1 homework is %2 for many student. Don't be worried.",)),) + pairs
# ( ) | Matches the expression inside the parentheses and groups it.
pairs = (("(.*) (hungry|sleepy)'", ("%1 %2",)),) + pairs
pairs = (("I have (.*) course", ("That is interesting @:@",)),) + pairs
pairs = (("I (.*) the course", ("Me too!",)),) + pairs
pairs = (("I feel (.*) today", ("Yeah, I am lisening, Could you tell more about your %1 feel",)),) + pairs
pairs = (("Do you have any idea about (.*)", ("I'm searching from Google",)),) + pairs
pairs = (("Can you tell (.*)", ("OK. I am working on that",)),) + pairs
pairs = (("(.*) project is hard", ("Let's try another method",)),) + pairs
pairs = (("Can you tell (.*)", ("OK. I am working on that",)),) + pairs

def eliza_chat():
    print("#"*70)
    print ("Initialize the chatbox")
    print("The numbers in the paris_list is:", len(pairs))
    print("--------Lisener for student--------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "Bye" when done.')
    print("#"*70)      
    print("Hello.  How are you feeling today?")

    nltk.chat.util.Chat(pairs, nltk.chat.util.reflections).converse()

def demo():
    eliza_chat()


if __name__ == "__main__":
    demo()