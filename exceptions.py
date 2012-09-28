"""test exceptions"""
def isfloat(f):
 try:
  float(f)
  return True
 except ValueError:
  return False
 except TypeError:
  return False
 except: 
  return

tests=[(4,4),'2342','adf','NaN','2341.3','4.5 what']

for t in tests:
 print(t,isfloat(t))

print()


while True:
  try:
    num=float(input('Enter the numerator: '))
    den=float(input('Enter the denominator: '))
  except ZeroDivisionError:
    print(" ->try again: can't divide by zero!")
  except:
    print(' ->type in real numbers this time.')
  else:
    break

try:
  'is this valid python'/7
except:
  print('Why cant I progam?')

#'try again'/7
