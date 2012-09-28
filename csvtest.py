
nextfilename='test.txt'
nextfile=open(nextfilename,'w')
for i in range(10):
  print('{0},{1},{2}'.format(i,i**3,i**4),file=nextfile)
nextfile.close()
