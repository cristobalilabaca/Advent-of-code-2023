def find_next_number(seq):
  if not any(seq):
    return 0

  aux = []

  for i in range(len(seq) - 1):
    aux.append(seq[i + 1] - seq[i])

  next_number = find_next_number(aux)

  return next_number + seq[-1]

with open('input9.txt', 'r') as f:
  lines = f.readlines()

extrapolation = 0

for i in lines:
  seq = i.strip('\n').split(' ')
  seq = list(map(int, seq))

  extrapolation += find_next_number(seq)

print(extrapolation)