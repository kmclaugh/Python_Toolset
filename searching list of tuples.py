# List of suits
suits=['clubs','diamonds','hearts','spades']
# List of faces
#numbercards=[list(range(2,10))]

numbercards=['2','3','4','5','6','7','8','9']
facecards=['ten','jack','queen','king','ace']
faces=numbercards+facecards
Deck=[]
for s in suits:
  for f in faces:
    Deck.append((f,s))
C=Deck[:]

from random import shuffle

Successes = 0
shuffle(C)
MyHand=C[:5]

handfaces=[x[0] for x in MyHand]
handsuits=[y[1] for y in MyHand]
twocount = handfaces.count('2')
ninecount = handfaces.count('9')
heartcount = handsuits.count('hearts')

if twocount+ninecount+heartcount != 0:
    Successes += 1

print(MyHand)
print(twocount)
print(ninecount)
print(heartcount)
print(Successes)
