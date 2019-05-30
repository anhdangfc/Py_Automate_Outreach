   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
'''
GENERATE RANDOM QUIZ

1. Create 35 different quizzes
2. 50 multiple-choice random order
3. 1 Correct answer and 3 wrong answers
4. Write the quizzes to 35 txt files
5. Write answer keys to 35 txt files

'''

## wd: Py_Automate
import os
import random

## 1 - Store the Quiz Data in a Dict
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
os.makedirs('Outputs\\Geo_Quizzes', exist_ok=True)

for quizNum in range(35):
    # Create the quiz and answer key files
    quizFile = open('Outputs\\Geo_Quizzes\\Num{}_Quiz.txt'.format(quizNum+1), 'w')
    ansKeyFile = open('Outputs\\Geo_Quizzes\\Num{}_Key_Ans.txt'.format(quizNum+1), 'w')
    # Write out the header of the quiz
    quizFile.write('Name:\nDate:\nResult:\n')
    quizFile.write( ('-'*10) + 'State Capital Quiz Form No.{}'.format(quizNum+1)+('-'*10))
    quizFile.write('\n\n')
    # Write out the header of the answer
    ansKeyFile.write( ('-'*10) + 'ANSWER: State Capital of Quiz Form No.{}'.format(quizNum+1)+('-'*10))
    ansKeyFile.write('\n\n')
    # Shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through 50 states making a question for each
    for questionNum in range(50):
        # Right answer
        correctAns = capitals[states[questionNum]]
        wrongAns = list(capitals.values()) ## take all cap
        del wrongAns[wrongAns.index(correctAns)] ## rm the right one
        wrongAns = random.sample(wrongAns, 3)
        AnsOptions = wrongAns + [correctAns] ## equiv to append
        random.shuffle(AnsOptions)
        # Write the question/options to quizFile
        quizFile.write(f'{questionNum+1}. What is the captial of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write('{0}. {1} \n'.format('ABCD'[i], AnsOptions[i]))
        quizFile.write('\n')
        # Write the correct Ans to ansKeyFile
        correct_ix = AnsOptions.index(correctAns) 
        ansKeyFile.write('Quiz {0}: {1}. {2} \n'.format(questionNum+1, 'ABCD'[correct_ix], AnsOptions[correct_ix]))


    # Close files
    quizFile.close()
    ansKeyFile.close()