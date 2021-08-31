print("\033[1;32;40m  \n")


#imports
import random
import time


#Variables
points = 0 
correct_answers = 0
wrong_answers = 0
rounds_played = 0
first_number = 0
second_number = 0
#functions, decoration
def question_creator():
  global first_number 
  global second_number
  if difficulty_levels == 1:
    first_number = random.randint(0,20) 
    second_number = random.randint(0,20)
  elif difficulty_levels == 2:
    first_number = random.randint(25,45)
    second_number = random.randint(25,45)
  elif difficulty_levels == 3:
    first_number = random.randint(50,100)
    second_number = random.randint(50,100)


def yes_no(question):
  valid = False
  while not valid:
    global yes_no_answer
    response = input(question).lower()
    if response == "yes" or response == "y":
      response = "yes"
      yes_no_answer = "yes"
      return " "
    elif response == "no" or response == "n":
      response = "no"
      yes_no_answer = "no"
      return " "
    else:
      print("Please answer yes / no")

def statement_generator(statement, decoration):
  sides = decoration * 3
  statement = "{} {} {}".format(sides, statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return " "



#Variable - User experience
statement_generator("welcome to MaQUIth", "●")
print(" ")
time.sleep(1)
userexperience = input(yes_no("Have you played MaQuith before ya dog? (y/n): "))
if yes_no_answer == "no":
  print(" ")
  input("instruction")
  input("instruction")
  print(" ")
      
#lists
difficulty_levels = ["1","2","3"]




#Tutorial


      
      

#Variables - Difficulty Of Questions
while True:
  try:
    difficulty_levels = int(input("What level of difficulty would you like to play? 1/2/3: "))
  except ValueError:
    print("put in a real level ya dog")
  except TypeError:
    print("level between 1 and 3 ya dog")
  else:
    break


#Amt of questions

#Questions & Answer Checkingto

#Gameplay
print(" ")
statement_generator("LEVEL {} QUESTIONS".format(difficulty_levels), "-")
print(" ")

while True:
  try:
    question_creator()
    user_answer = int(input("what is " + str(first_number) + " + " + str(second_number) + "? " ))
    if user_answer == 000:
      statement_generator("FINAL POINTS {}".format(points), "◌")
      break
    if user_answer == first_number + second_number:
      print(" ")
      statement_generator("well done! its right", "R")
      print(" ")
      statement_generator("point added +1", "-")
      rounds_played += 1 
      correct_answers += 1
      points += 1 
    elif user_answer != first_number + second_number:
      statement_generator("Too bad, its wrong", "W")
      statement_generator("point not added +0", "-")
      rounds_played += 1 
      wrong_answers += 1
  except ValueError:
    print("only numbers ya dog") 
    

