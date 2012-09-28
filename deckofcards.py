# List of suits
suits=['clubs','diamonds','hearts','spades']
# List of faces
#numbercards=[list(range(2,10))]

numbercards=[str(x) for x in range(2,10)]

#numbercards=['2','3','4','5','6','7','8','9']

facecards=['ten','jack','queen','king','ace']

faces=numbercards+facecards


Deck=[]
for s in suits:
  for f in faces:
    Deck.append((f,s))

print(Deck)
print('we have',len(Deck),'cards')

# Shuffle the deck
C=Deck[:]

from random import shuffle

shuffle(C)

print(C,len(C))

# Deal out five cards from the deck

# deal from the end of the deck.
MyHand=C[-5:]
C=C[:-5]
print(MyHand,len(MyHand))
print(C,len(C))

