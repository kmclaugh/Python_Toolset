import pickle

l = []
f = '/Users/kevin/Library/Jarvis/JarvisMail/jmail_new_messages.dat'
file = open(f,'wb')
pickle.dump(l,file)
file.close()
