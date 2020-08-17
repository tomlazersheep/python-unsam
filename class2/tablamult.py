counters = [0]*10
print('-------------------------------------------')
print('  ',''.join(f"{j:4d}" for j in range(10)))
print('-------------------------------------------')
for n in range(9):
  for i,counter in enumerate(counters):
    counters[i] += i
  print(f'{n}:', ''.join(f"{x:4d}" for x in counters))
