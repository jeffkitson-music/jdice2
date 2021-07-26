# 🎲 jdice2
Python implementation of diceware using the bip39 wordlist.

## :books: About
Generate a pseudorandom phrase from the bip39 wordlist for passphrases or seed phrases. 

Inspiration: 
- [xkcd: correct horse battery staple](https://xkcd.com/936/)
- [Dr. Mike Pound's](https://github.com/mikepound) video for Computerphile on [how to choose a password](https://www.youtube.com/watch?v=3NjQ9b3pgIg). 

## :eyes: Usage
```python
import jdice2
phrase = jdice2.getwords(12)
print(phrase)
```

## :warning: Disclaimer
This is a hobby project and a proof-of-concept. Do not use this to generate real passwords or seed phrases. [Pseudorandom isn't random](https://simplicable.com/new/pseudorandom-vs-random).

## :mega: Credits
- [taelfrinn](https://github.com/taelfrinn/) for the original [analog implementation](https://github.com/taelfrinn/Bip39-diceware) (physical dice and coin).
