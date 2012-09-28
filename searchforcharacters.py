
test='100000000000*10000000=10'



def findoperand(equation):
    a = 0
    b = 0
    for i in equation:
        if i != '=':
            b += 1
        else:
            equalloc=b
        if i >= '0':
            a += 1
        else:
            operand = i
            operandloc = a
    return(operand,operandloc,equalloc)




equationinfo = findoperand(test)
operand = equationinfo[0]
operandloc = equationinfo[1]
equalloc = equationinfo[2]

num1=int(equation[0:operandloc])
operand=operand
num2=int(equation[(operandloc+1):equalloc])
answer=int(equation[(equalloc+1):])


print(operand)
print(operandloc)
print(equalloc)
print(num1)
print(num2)
print(answer)
