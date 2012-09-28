import pickle

List = ["movies","bread","LOTR"]

outfile = open("pickle.txt", "wb")
pickle.dump(List, outfile)
outfile.close()

infile = open('pickle.txt','rb')
newlist = pickle.load(infile)
