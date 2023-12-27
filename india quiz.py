import time
import pygame
from pygame import mixer

pygame.mixer.init()
wrong_sound = pygame.mixer.Sound('C:/Users/Admin/Downloads/buzzer.wav')
correct_sound = pygame.mixer.Sound('C:/Users/Admin/Downloads/correct.wav')

pygame.init()
mixer.music.load('C:/Users/Admin/Downloads/background_music.wav')
mixer.music.play(-1)

#Welcome the user
print("Welcome to the Simple Quiz Game! ")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chances to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)
      
#Score                    
score = 0

#question 1
question_1 = print("1) What is the capital of India?\n(a) Bangalore\n(b) Mumbai\n(c) New Delhi\n(d) Chennai\n\n ")
answer_1 = "c"

for i in range(chances) :
      answer = input("Answer: ")
      if (answer.lower() == answer_1):
          print("Correct! Good Job.\n")
          score = score + 1
          correct_sound.play()
          break
      else:
        print("Incorrect!\n ")
        time.sleep(0.5)
        wrong_sound.play()
        print("The correct answer is", answer_1, "\n\n ")

time.sleep(2)        

#question 2
question_2 = print("2) What is the national animal?\n(a) Lion\n(b) Monkey\n(c) Snake\n(d) Tiger\n\n ")
answer_2 = "d"

for i in range(chances) :
      answer = input("Answer: ")
      if (answer.lower() == answer_2) :
          print("Correct! Good Job.\n")
          score = score + 1
          correct_sound.play()
          break
      else:
        print("Incorrect!\n ")
        time.sleep(0.5)
        wrong_sound.play()
        print("The correct answer is", answer_2, "\n\n ")
        
time.sleep(2)

#question 3
question_3 = print("3) When is Independence day celebrated?\n(a) January 21\n(b) August 15\n(c) November 14\n(d) December 25\n\n ")
answer_3 = "b"

for i in range(chances) :
      answer = input("Answer: ")
      if (answer.lower() == answer_3) :
          print("Correct! Good Job.\n")
          score = score + 1
          correct_sound.play()
          break
      else:
        print("Incorrect!\n ")
        time.sleep(0.5)
        wrong_sound.play()
        print("The correct answer is", answer_3, "\n\n ")
        
time.sleep(2)

#print the score
while score >= 2:
    print("Well done! Your score is", score)
    break

while score < 2:
    print("Better luck next time! Your score is", score)
    break

time.sleep(2)

#Goodbye message
print("Thank you for playing the Simple Quiz Game!")

time.sleep(2)
