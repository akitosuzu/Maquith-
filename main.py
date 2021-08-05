print("\033[1;32;40m  \n")


#imports
import random
import time


#Variables
points = 0 
correct_answers = 0
wrong_answers = 0
rounds_played = 0
#functions, decoration
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

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



  print(top_bottom)
  print(statement)
  print(top_bottom)

def statement_generator2(statement, decoration):
  sides = decoration * 2
  statement = "{} {} {}".format(sides, statement,sides)
  
  print(statement)

  return " "

  print(statement)


#Variable - User experience
statement_generator("welcome to MaQUIth", "#")
print()
print(" ")
time.sleep(1)
yes_no("Have you played MaQuith before ya dog? (y/n): ")
print(" ")
    
  
#lists
difficulty_levels = ["1","2","3"]


print("kkk")

#Tutorial


      
      

#Variables - Difficulty Of Questions

while True:
  try:
    difficulty_levels = int(input("What level of difficulty would you like to play? 1/2/3: "))
  except ValueError:
    print("put in a real level ya dog")
  except TypeError:
    print("level between 1 and 3 ya dog")




    



#Amt of questions
  

#Questions & Answer Checking

#Gameplay
  if difficulty_levels == 1:
    first_number = random.randint(0,20) 
    second_number = random.randint(0,20)
    break
  elif difficulty_levels == 2:
    first_number = random.randint(25,45)
    second_number = random.randint(25,45)
    break
  elif difficulty_levels == 3:
    first_number = random.randint(50,100)
    second_number = random.randint(50,100)
    break
while True:
  try:
    user_answer = int(input("what is " + str(first_number) + " + " + str(second_number) + "? " ))
    if user_answer == first_number + second_number:
      print(" ")
      statement_generator("well done! its right", "R")
      print(" ")
      statement_generator2("point added +1" "-")
      rounds_played += 1 
      correct_answers += 1
      points += 1 
    elif user_answer != first_number + second_number:
      statement_generator("Too bad, its wrong", "W")
      statement_generator2("point not added +0", "-")
      rounds_played += 1 
      wrong_answers += 1 
  except ValueError:
    statement_generator("Only Number Please", "!")
  else:
    break