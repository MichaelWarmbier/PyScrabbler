### Programmed by Michael Warmbier ###

### Libraries ###

import re 

##### Data Storage #####

with open('Collins Scrabble Words (2019).txt') as file:
    wordList = file.read().splitlines()

# Constant letter point values
class letters:
  values = [[' '], 
            ['A','E','I','L','N','O','R','S','T','U'],
            ['D','G'],
            ['B','C','M','P'],
            ['F','H','V','W','Y'],
            ['K'],
            [],
            [],
            ['J','X'],
            [],
            ['Q','Z']];

class tempMemory:
  def __init__(self):
    self.storedLetters = []
    self.scannedLetters = []

##### Methods #####

# Returns point value of a specific letter
def getLetterValue(letter):
  for value in letters.values:
    if letter.upper() in letters.values[letters.values.index(value)]:
      return letters.values.index(value);
  raise Exception('Argument is NOT a valid Scrabble letter.');

def getWordValue(word):
  finalValue = 0;
  for char in word:
    finalValue += getLetterValue(char);
  return finalValue;
    

# Gets all possible words given provided letters
def getWords(letters):
  regex = re.compile('^([' + letters.upper() + '])*$');
  validWords = [];
  for word in wordList:
    if regex.match(word):
      validWords.append(word);
  for word in validWords:
    tLetters = letters
    for char in word:
      tLetters.replace(char, '')
      
  return validWords;
    
##### Test Code #####

storedWords = getWords('juhsine');
for word in storedWords:
  print(word + ' ' + str(getWordValue(word)))