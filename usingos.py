#!/usr/bin/env python3
import os

#environ
print('home=',os.environ['HOME'])
print('path=',os.environ['PATH'])
print('hostname=',os.environ['HOSTNAME'])

print(os.listdir())
#os.chdir(path)
#os.listdir(path='.')
os.chdir('testdir')
print(os.listdir())
os.chdir('..')
print(os.listdir())

#os.walk()
for dirpath, dirnames, filenames in os.walk('.'):
 print(dirpath,dirnames,filenames)
 for f in filenames: 
  print(f)


#os.mkdir(path[, mode])
#os.mkdir('testdir5')

#os.makedirs(path, mode=0o777, exist_ok=False)
#os.makedirs('t1/t2/t3/t4/t4')
#os.mkdir('a1/a2/a3')

#os.rename(src, dst)
#os.rename('testdir','newtestdir')


#os.rmdir(path)


#os.path.join
for dirpath, dirnames, filenames in os.walk('.'):
  h=os.path.split(dirpath)
  print(h)
  h2=os.path.join(h)
  print(h2)


