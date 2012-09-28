#read a file line by line
filename="forloopexamples.py"
print('--------'+filename+'---------')
f=open(filename)
for g in f:
  print(g,end="")
f.close()

# what happens if I leave end unspecified
print('--------'+filename+' no end--------')
f=open(filename)
for g in f:
  print(g)
f.close()


# use os to print out a file

print('--------'+filename+'using os -------')
import os
os.system('cat '+filename)


#we can use open directly
print('--------'+filename+' with line numbers ---------')
i=1
for g in open(filename):
  print(i,":",g,end='',sep='')
  i+=1


# we can read the whole file in at once

lines=open(filename).readlines()
print('--------'+filename+' as a list --------')
print(lines)
print('--------'+filename+'---------')
for x in lines:
 print(x,end='')


# lets create a file

newfilename='ournewfile.txt'
newfile=open(newfilename,'w')

for i in range(12):
  print(i,'8'*i,file=newfile)
# test whether this is necessary
newfile.close()


#and read it back
thenewfile=open(newfilename)
print('--------'+newfilename+'---------')
for l in thenewfile:
  print(l,end='')



# lets do comma separated values (CSV)

nextfilename='nextcsvfile.txt'
nextfile=open(nextfilename,'w')
for i in range(10):
  print('{0},{1},{2}'.format(i,i**2,i**3),file=nextfile)
nextfile.close()


#and read it back
thenextfile=open(nextfilename)
print('--------'+nextfilename+'---------')
for l in thenextfile:
  line=l.strip()
  vals=line.split(',')
  print(vals)
  nums=[int(v) for v in vals]
  print(nums)
