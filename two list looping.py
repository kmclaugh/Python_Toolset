
f=open('/Users/kevin/Desktop/text1.txt','r')
g=open('/Users/kevin/Desktop/text2.txt','r')

list1 = []
list2 = []
for linef, lineg in zip(f,g):
    if len(linef) > len(lineg):
        list1.append(linef.rstrip('\n'))
        list2.append(lineg.rstrip('\n'))
words = []

for x, y in zip(list1,list2):
    lx=len(x)
    ly=len(y)
    difference = lx-ly
    a = 0
    while a <= (ly-1):
        if x[a] != y[a]:
            words.append(x[a:(a+difference)])
            a = (ly-1)
        elif a == (ly-1):
                words.append(x[ly:lx])
        a += 1
print(words)

