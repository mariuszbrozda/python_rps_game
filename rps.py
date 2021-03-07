
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print('\nWelcome in ROCK, PAPER, SCISSORS game !')
print('\n RULES OF THE GAME: \n Rock wins against scissors. \n Scissors win against paper. \n Paper wins against rock.\n')

player_name = input('Please type your name ')

print(f'{player_name}, to play the game simply type \n 0 for "ROCK" \n 1 for "SCISSORS"\n 2 for "PAPER"')


player_points = 0
computer_points = 0

player_choice = int(input('My choice: '))
computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
  print('You typed invalid number - You lose! ')
else:
  game = [rock, paper, scissors]
  player_selection = game[player_choice]
  computer_selection = game[computer_choice]

  print(f'{player_name}: {player_choice} {player_selection} ')
  print(f'Computer: {computer_choice} {computer_selection} ')

  if player_selection == rock and computer_selection == scissors:
    player_points += 1
    print(f'RESULTS: {player_name} WINS')
  elif computer_selection == rock and player_selection == scissors:
    computer_points += 1
    print('RESULTS: Computer WINS')

  elif player_selection == scissors and computer_selection == paper:
    player_points += 1
    print(f'RESULTS: {player_name} WINS')
  elif computer_selection == scissors and player_selection == paper:
    computer_points += 1
    print('RESULTS: Computer WINS')

  elif player_selection == paper and computer_selection == rock:
    player_points += 1
    print(f'RESULTS: {player_name} WINS')
  elif computer_selection == paper and player_selection == rock:
    computer_points += 1
    print('RESULTS: Computer WINS')
  elif computer_selection == player_selection:
    print('RESULT: DRWAW')


print(f'POINTS: {player_name}: {player_points} - Computer: {computer_points}')
