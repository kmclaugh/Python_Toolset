import pickle

l = []
f = '/Users/kevin/Library/Jarvis/JarvisMail/jmail_querry_list_send_rachael_update_checker.dat'
file = open(f,'wb')
pickle.dump(l,file)
file.close()
