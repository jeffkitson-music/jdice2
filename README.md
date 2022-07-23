# 🎲 jdice2
Python implementation of diceware using the bip39 wordlist.

## :books: About
Generate a pseudorandom phrase from the bip39 wordlist for passphrases or seed phrases. This script implements [Arman the Parman's method](https://armantheparman.com/dicev2/) to derive the seed phrase. 

**Note**: The old method of simulating actual dice is found in the "old" folder. 

Inspiration: 
- [xkcd: correct horse battery staple](https://xkcd.com/936/)
- [Dr. Mike Pound's](https://github.com/mikepound) video for Computerphile on [how to choose a password](https://www.youtube.com/watch?v=3NjQ9b3pgIg). 

## :eyes: Usage
```python
import jdice2


seed_phrase = jdice2.get_bip39()
print(seed_phrase)
# helmet distance wedding frequent chunk burst, etc...


# Other utilities

# returns full word based on first four chararcters
ff = "corr"
full_word = jdice2.first_four(ff)
print(full_word)
# correct


# returns a randomly generated password - Not wordlist related, just convenient
password = jdice2.generate_password(passwordlength=16)
print(password)
# EfYZ<8L,9PeyM??f
```

## :warning: Disclaimer and Security Warnings
- This is a hobby project, proof-of-concept, and for learning purposes only. 
- **Do not use this to generate real seed phrases.** 
- [Pseudorandom isn't random](https://simplicable.com/new/pseudorandom-vs-random).
- If you do proceed at your own risk, heed the usual warnings about generating passwords and seed phrases securely in a **fully offline, air-gapped environment.** 
- Need something full-featured? Try Ian Coleman's [bip39 tools](https://iancoleman.io/bip39/).


## :mega: Credits
- [taelfrinn](https://github.com/taelfrinn/) for the original [analog implementation](https://github.com/taelfrinn/Bip39-diceware) (physical dice and coin).
- [armantheparman](https://armantheparman.com/) for [this article](https://armantheparman.com/bitcoin-seed-with-dice/) on how to correctly generate a bip39-compliant seed phrase from dice including the checksum/last word.
