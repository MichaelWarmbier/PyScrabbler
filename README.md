# PyScrabbler

A Python package for retrieving a list of valid words and their values in Scrabble™ given a set of letters [seven to fifteen].

**Important**: Project is still in its pre-release stage.

## Description

### Methods

`getScrabbleWords(letters)`:

**Parameter**: _String_; provided letters.<br>
**Returns**: _2D-List_; words and their base values.<br>

**Exceptions**:<br>
&emsp;`Error: Letter count must be between seven and fifteen.`: occurs when provided _String_ is less than seven/longer than fifteen characters.

**Example Use**:

```py
storedWords = getWords('JUHSINE')
for word in storedWords:
  print(word)
```

**Example Output**:

```
['EH', 5]
['EHS', 6]
['EISH', 7]
['EN', 2]
['ENS', 3]
['ES', 2]
['HE', 5]
['HEN', 6]
['HENS', 7]
...
```

## Installation

Coming soon!

## Legal

This project was developed for educational purposes. I do not own, nor claim to own, anything involving Scrabble™. Scrabble™ is a trademark owned by Hasbro Inc and all rights are reserved to its respective owner.
