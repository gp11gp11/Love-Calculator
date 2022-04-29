'''
you are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

together_name = name1+name2
lowercasing = together_name.lower()

t = lowercasing.count("t")
r = lowercasing.count("r")
u = lowercasing.count("u")
e = lowercasing.count("e")

true = t+r+u+e
l = lowercasing.count("l")
o = lowercasing.count("o")
v = lowercasing.count("v")
e = lowercasing.count("e")
love = l+o+v+e


score = str(true)+str(love)
score_int = int(score)
if score_int <10 and score_int>90:
    print(f"Your score is {score}, you go together like coke and mentos")
if score_int>40 and score_int<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")