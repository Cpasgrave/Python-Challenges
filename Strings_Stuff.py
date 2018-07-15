"""
This is my answer to :
CHALLENGE: Strings stuff
proposed by QuentinJanuel
https://www.sololearn.com/Discuss/993086/challenge-strings-stuff

Hi there, I found a challenge for you:

The function takes 2 strings and returns false only if there is no way for you to:
- choose a character index in the 2nd string as your starting point,
- keep moving to the right or left char,
- keep going until you eventually have read the 1st string.

For instance:
- "dcdcb" in "abcde", I can start at the 4th char ("d"), and do the following moves: ←→←←, so that at the end I got "dcdcb". It is possible, returns true.
- "ac" in "abc", no solution exists, it returns false.

Good luck!"""

# ---------------------------------------
# ---------------------------------------

# test cases :

testcases = [["kayaks", "skay"],["bit", "bite"],["code", "coddle"],["atatata", "ta"],["trirtotrtopip", "tptirtopit"], ["abcbcbab", "abcba...cba"]]

# function :

def read(words):
    
 a = words[0] ; b = "*"+ words[1]+"*"
 paths = {p for p, c in enumerate(b) if c == a[0]}
    
 while True:
  temp = [p for p in paths]
  a = a[1:]
  for t in temp:
   if a == "": return "True"
   if b[t-1] == a[0]:paths.add(t-1)
   elif b[t+1] == a[0]: paths.add(t+1)
   paths.remove(t)
   if len(paths)==0:return "False"

# just printing the results when applying the function to our testcases :

[[print(words[0],"-", words[1],"->",read(words),"\n")] for words in testcases]

# ---------------------------------------
# ---------------------------------------

# The method used in this code :

'''
- First I call a the left word and b the right word

- Then I add stars "*" before and after the second word
  -> ex: a becomes "kayaks" and b  "*skay*"
   
- The stars are added to let the index -1 and index +1
  be usable from any letter in the word 
  (no index out of range error returned)
  of course, it wouldn't work if a or b initially
  contains the "*" character. This depends on the words tested, 
  you cans choose anything instead of *, just need to know
  what character is never used in the testcase strings.
  There also could be an additional line of code checking that,
  but ... well
   
- Then the engine of the code happens within {paths}
  paths is a set. It will follow the multiple possible 
  "reading paths". It is first defined as a set containing
  the indexes for each occurence of the first character of a in b.
  ex : a="kayaks" b="*skay*" paths={2} (1st character is "k")
  ex : a="abcbcbab" b="*abcba...cba*" paths={1, 5, 11}
  ex : a="trirtotrtopip" b="*tptirtopit*" paths={1, 3, 6, 10} (1st character is "t")
   
- The processing then starts with a wile True (infinite loop)
  this loop will stop by returning "True" at line 38
  or returning "False" at line 64
    
- The idea here is simple :
  For each position in paths, check if the next 
  character in a can be found next to the actual 
  character.
  ex : in "kayaks", the reader is at {2}, reading "k"
      so we want to check if b[1] or b[3] is the
      next character in a, which is "a"
  After doing so, then the paths set has to be updated
  from {2} becoming {3} because "a" is found at position
  3 in b.
  It's nice because this allows to fork paths if the
  letter is found both left and right like in firosuke's
  "abcbcbab", "abcba...cba" test case. 
  
  Lets follow this test case :
        
  a="abcbcbab", b="*abcba...cba*" 
  first : char "a" --> paths={1, 5, 11}
  next : char "b" --> paths={2, 4, 10}
  next : char "c" --> paths={3, 9}
  it's interesting at this point to see that two paths 
  lead to the same point, we don't need to follow two paths.
  If this goes till the end, it will return "True", it would 
  need some addition to the code if we wanted to be able to 
  check how many paths are possible.
  next : char "b" --> paths={2, 4, 10}
  Here there is a fork, two possiblme directions from position
  3 when next character is "b"
  next : char "c" --> paths={3, 9}
  next : char "b" --> paths={2, 4, 10}
  next : char "a" --> paths={1, 5, 11}
  because paths is not empty and we arrived to the last character
  the answer returned will be "True"
  
  an other test case :
  "code", "*coddle*"
  first : char "c" --> paths={1}
  next : char "o" --> paths={2}
  next : char "d" --> paths={3}
  next : char "e" --> paths={}
  an empty path immediately returns "False"
  
- Technically, to do what I showed just above,
  I had to create a temp list called temp by copying 
  the paths set. This is because the for loop
  is taking steps from temp ( for t in temp, line 37 )
  modifying paths.
  It couldn't take steps from paths and modify 
  paths at the same time (which is the goal)
  
- Each round of the loop, a is shortened from its first letter
  then comes the check : if a is empty, end of word, "True"
  lines 39 - 41 are updating paths
  and finally there's the check to see if paths is empty
  if it's the case, "False" is returned.'''
  
