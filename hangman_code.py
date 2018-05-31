# hangman.py
# Name: NEHA PURI
# Hangman Game
import random
import string

WORDLIST_FILENAME = "words.txt"
#WORDLIST_FILENAME = "word_try.txt"
def load_words():

  print("Loading word list from file...")
  # inFile: file
  inFile = open(WORDLIST_FILENAME, 'r')
  # line: string
  line = inFile.readline()
  # wordlist: list of strings
  wordlist = line.split()
  print("  ", len(wordlist), "words loaded.")
  return wordlist

def is_word_guessed(secret_word, letters_guessed):
  #secret_word = list(secret_word)
  #return (secret_word == letters_guessed)

  for char in secret_word:
      if char not in letters_guessed:
        return False
  return True

def get_guessed_word(secret_word, letters_guessed):
    l = []
    for word in secret_word:
      if word in letters_guessed:
        l.append(" "+word)
      else:
        l.append(" "+'-')
    l_str = ''.join(l)  
    return l_str

def get_available_letters(letters_guessed):
    available_letters = []
    for i in string.ascii_lowercase:
      if i in letters_guessed: 
        pass
      else:  
        available_letters.append(i)
    remaining_letters = ''.join(available_letters) 
    return remaining_letters 
      
   
def choose_word(wordlist):
  return random.choice(wordlist)
   
def hangman(secret_word):
  Warning = 3
  guesses = 6
  message = " "
  letters_guessed = []
  print('Welcome to the game Hangman!')
  print('I am thinking of a word that is',len(secret_word),'letter long')
  print('you have ',guesses,' guesses ')
  print('you have ',Warning,' warnings ')
  print(get_guessed_word(secret_word,letters_guessed))
  print('Available letters are ',get_available_letters(letters_guessed))

  
  while guesses > 0 and not is_word_guessed(secret_word,letters_guessed):
    print('_'*50)
    entered_letters = input('Enter a Letter ')
    if not str.isalpha(entered_letters): 
      message = 'not a letter!!'
      if Warning > 0:
        Warning -= 1
        print('Warning Left ',Warning)
      else:
        guesses -= 1 
    else:
      entered_letters = str.lower(entered_letters)
      if entered_letters in letters_guessed:
        message = 'already entered'
        if Warning > 0:
          Warning -= 1
          print('Warning Left ',Warning)
        else:
          guesses -= 1
          print('guesses left',guesses)
      else:
        letters_guessed.append(entered_letters)
        if entered_letters in secret_word:
          message = 'good guess'
        else:
          guesses -= 1 
          message = 'oops letter not present '
    print('Available letters are ',get_available_letters(letters_guessed))      
    print(message, get_guessed_word(secret_word,letters_guessed))   
    print('Warning Left ',Warning)          
    print('guesses left',guesses)
  if is_word_guessed(secret_word,letters_guessed):
    print('Congratulations you won!!')
    print('Total Score ',Total_score())
  else:
    print('The Secret letter was ',secret_word)  



def match_with_gaps(my_word, other_word):

  my_word = my_word.strip()
  other_word = other_word.strip()
  my_word_new = my_word.replace(' ','')
  other_word_new = other_word.replace(' ','')

  if len(my_word_new) != len(other_word_new):
    return False

  i = 0
  my_word_list = list(my_word_new)
  other_word_list = list(other_word_new)
  for letter in my_word_list:
    if letter != '_':
      if my_word_list.count(letter) != other_word_list.count(letter):
        return False
      if letter != other_word_list[i]:
        return False
    i += 1
  return True  

def show_possible_matches(my_word):
  
  hints_available = []
  matches = False
  for word in wordlist:
    if match_with_gaps(my_word, word):
      hints_available.append(word)
      matches = True    

  if matches:
      print("Possible matches are: ")
      print(','.join(hints_available))
  else:
      print("no matches found")
  return ','.join(hints_available)   



def find_unique_letters():
  unique_letters = []
  for char in secret_word:
    if char not in unique_letters:
      unique_letters.append(char)
    else:
      pass
  return len(unique_letters)


def Total_score():
  total_unique_letters = find_unique_letters()
  print('total unique letter are :',total_unique_letters)
  return 2*total_unique_letters 
    

if __name__ == "__main__":
  wordlist = load_words()
  secret_word = choose_word(wordlist)
  hangman(secret_word)
