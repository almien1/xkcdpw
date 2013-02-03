#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Password generator, inspired by http://xkcd.com/936/ 
# Originally posted as comment to stackoverflow #7479442
#-----------------------------------------------------------------------------
# (c) Oliver White, 2012-2013
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#-----------------------------------------------------------------------------
import random
import re

# apt-get install wbritish
def randomWords(num, dictionary="/usr/share/dict/british-english"):
  r = random.SystemRandom() # i.e. preferably not pseudo-random
  f = open(dictionary, "r")
  count = 0
  chosen = []
  for i in range(num):
    chosen.append("")
  prog = re.compile("^[a-z]{5,9}$") # reasonable length, no proper nouns
  if(f):
    for word in f:
      if(prog.match(word)):
        for i in range(num): # generate all words in one pass thru file
          if(r.randint(0,count) == 0): 
            chosen[i] = word.strip()
        count += 1
  return(chosen)

def genPassword(num=4):
  return(" ".join(randomWords(num)))

if(__name__ == "__main__"):
  print genPassword()
