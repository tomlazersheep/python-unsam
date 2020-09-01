# Mostrar los 10 primeros numeros perfectos
numeros_perfectos = []
candidato = 5

while len(numeros_perfectos) < 10:
  divisores = 0

  for i in range(1,candidato):
    if (candidato % i) == 0:
      divisores += i
  if divisores == candidato:
    numeros_perfectos.append(candidato)
  candidato += 1

print(numeros_perfectos)
