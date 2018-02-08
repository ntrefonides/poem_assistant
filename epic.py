
#rhyming


#below is original list so that can be recovered after after code depletes  it
#A = ["take me to the mountain gate","whom the higher crows berate"]
#B = ["left to fancy the decay", "the mountain man, the mounting way" ]
#C = ["in the ocsillating sky", "your the cabbage of my eye"]



A = ["take me to the mountain gate","whom the higher crows berate","I'm gangly with a gangly gate", "the gun it triggered late"," "]
B = ["left to fancy the decay", "the mountain man, the mounting way","there's a bucket there's beday","there is nothing i wont say"," "]
C = ["in the ocsillating sky", "your the cabbage of my sty", "fadad with the jaded die","another truths another lie"," "]
D = ["damn the moon to craters","fuck boy I'm a hater", "waiting on the waiters"," "]
E = ["lost in all directions", "searching for the loser section", "I'll find my spleen in this disection"," "]
F = ["I'm gone with wind and snow", "lost but I didnt know", "I told her that I'll never show"," "]
G = ["glancing at my compass", "peter piped her pompass", "this baby lumps a lumpus"," "]
H = ["gliding in the dark", "bless the fuckin' narc", "steal the donkeys from the arc"," "]
I = ["I've died I'll die again", "these eggs their hatching hens", "who what where why when"," "]






#creates a seven line stanza with randomly selected rhyme scheme consisting of any combination of A, B, and C rhymes
import random 

all_lines = [A,B,C,D,E,F,G,H,I] 
length_stanza =7
number_of_stanzas = 2


for n in range (number_of_stanzas):
  rhyme_set = random.sample(all_lines,3)
  print('\n') 
  for n in range (length_stanza):
    i = random.choice(rhyme_set)
    if len(i) > 0:
      random.sample(i,1)
      print(i[-1])
      del i[-1]

