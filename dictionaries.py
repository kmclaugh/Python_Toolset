games={'x':'home','y':'away'}

print(games)

for g in games:
 print(g,games[g])


del games['x']

print(games)

if not games.get('z'):
  games['z']='something'

if 'z' in games:
  print(games['z'])
