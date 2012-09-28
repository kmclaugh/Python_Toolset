# let's load in the words file 
import time

wordlistfilename='/usr/share/dict/words'

t1=time.time()
print(t1)
f=open(wordlistfilename)
wordlist=[]
count=0
for line in f:
  wordlist.append(line.strip())
  count +=1

t2=time.time()
print('there are {} words in {}'.format(count,wordlistfilename))
print('reading the file took {:6.4f} seconds'.format(t2-t1))
f.close()

# version 2
t1=time.time()
wordlist=open(wordlistfilename).readlines()
t1a=time.time()
for i in range(len(wordlist)):
  wordlist[i]=wordlist[i].strip()
t2=time.time()

print('there are {} words in {}'.format(len(wordlist),wordlistfilename))
print('reading the file took {:6.4f} seconds'.format(t1a-t1))
print('reading + removing newlines took {:6.4f} seconds'.format(t2-t1))


# selecting based on a test:
# let's get only the three to eight letter words, lowercase

middlewords=[]
mwmin=3
mwmax=8

for l in wordlist:
  if mwmin<=len(l)<=mwmax and l[0].islower():
    middlewords.append(l)

mwcount=len(middlewords)

print('there are {} non-proper words with between {} and {} letters'.format(mwcount,mwmin,mwmax))
