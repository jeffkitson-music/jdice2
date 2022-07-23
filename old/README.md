# 🎲 jdice2 - Old Method
Python implementation of diceware using the bip39 wordlist.

## :books: About
Generate a pseudorandom phrase from the bip39 wordlist for passphrases or seed phrases. The method uses a coin flip and four six-sided die to generate a key (h1111 - t4362) that's paired with a word on the wordlist. In this implementation five dice are used, with the first die simulating the coin flip. Even numbers are heads and odds are tails. 

Note: getbip39() is the **only** function that gives a bip39-compliant seed phrase. The other functions just pull random words and do **not** implement the last word checksum. This repo is really just for learning purposes and not intended for serious use. Please heed the usual warnings about generating passwords and seed phrases securely offline, etc. Need something full-featured? Try Ian Coleman's [bip39 tools](https://iancoleman.io/bip39/).

Inspiration: 
- [xkcd: correct horse battery staple](https://xkcd.com/936/)
- [Dr. Mike Pound's](https://github.com/mikepound) video for Computerphile on [how to choose a password](https://www.youtube.com/watch?v=3NjQ9b3pgIg). 

## :eyes: Usage
```python
import jdice2


# returns a string of words. n is the number of words you want
# Note: This is NOT bip39-compliant. It's just random words
phrase = jdice2.getwords(n=12)
print(phrase)
# educate noodle history team arctic resource worth random box endless engage unveil


# returns as a python list
wordlist = jdice2.getwordlist(4)
print(wordlist)
# ['educate', 'noodle', 'history', 'team']


# returns a 24-word bip39-compliant seed phrase
bip39_seed_phrase = jdice2.getbip39()
print(bip39_seed_phrase)
# helmet distance wedding frequent chunk burst, etc...


# returns full word based on first four chararcters
ff = "corr"
full_word = jdice2.firstfour(ff)
print(full_word)
# correct


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


# returns a randomly generated password
# Not wordlist related, just convenient
password = jdice2.generate_password(passwordlength=16)
print(password)
# EfYZ<8L,9PeyM??f
```

## :warning: Disclaimer
This is a hobby project and a proof-of-concept. Do not use this to generate real passwords or seed phrases. [Pseudorandom isn't random](https://simplicable.com/new/pseudorandom-vs-random).

## :mega: Credits
- [taelfrinn](https://github.com/taelfrinn/) for the original [analog implementation](https://github.com/taelfrinn/Bip39-diceware) (physical dice and coin).
- [armantheparman](https://armantheparman.com/) for [this article](https://armantheparman.com/bitcoin-seed-with-dice/) on how to correctly generate a bip39-compliant seed phrase from dice including the checksum/last word.
