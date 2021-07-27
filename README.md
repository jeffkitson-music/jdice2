# 🎲 jdice2
Python implementation of diceware using the bip39 wordlist.

## :books: About
Generate a pseudorandom phrase from the bip39 wordlist for passphrases or seed phrases. The method uses a coin flip and four six-sided die to generate a key (h1111 - t4362) that's paired with a word on the wordlist. In this implementation five dice are used, with the first die simulating the coin flip. Even numbers are heads and odds are tails. 

Inspiration: 
- [xkcd: correct horse battery staple](https://xkcd.com/936/)
- [Dr. Mike Pound's](https://github.com/mikepound) video for Computerphile on [how to choose a password](https://www.youtube.com/watch?v=3NjQ9b3pgIg). 

## :eyes: Usage
```python
import jdice2


# Returns a string of words. n is the number of words you want
phrase = jdice2.getwords(n=12)
print(phrase)
# educate noodle history team arctic resource worth random box endless engage unveil


# Returns as a python list
wordlist = jdice2.getwordlist(4)
print(wordlist)
# ['educate', 'noodle', 'history', 'team']


# returns single word based on the diceware code.
word = jdice2.getword("h2555")
print(word)
# correct


# returns the diceware code based on the word
code = jdice2.getcode("horse")
print(code)
# h5133


# returns a python list of codes based on a list of words
xkcd = ["correct","horse","battery","staple"]
code_list = jdice2.getcodelist(xkcd)
print(code_list)
# ['h2555', 'h5133', 'Word not in list!', 'Word not in list!']
```

## :warning: Disclaimer
This is a hobby project and a proof-of-concept. Do not use this to generate real passwords or seed phrases. [Pseudorandom isn't random](https://simplicable.com/new/pseudorandom-vs-random).

## :mega: Credits
- [taelfrinn](https://github.com/taelfrinn/) for the original [analog implementation](https://github.com/taelfrinn/Bip39-diceware) (physical dice and coin).
