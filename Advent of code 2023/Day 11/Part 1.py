with open('input11.txt', 'r') as f:
  lines = f.readlines()

matrix = []

for i in lines:
  matrix.append(list(i.strip('\n')))

  if '#' not in i:
    matrix.append(list(i.strip('\n')))

transposed_matrix = list(map(list, zip(*matrix)))

expanded_transposed = []

for i in transposed_matrix:
  expanded_transposed.append(list(i))

  if '#' not in i:
    expanded_transposed.append(list(i))

matrix = list(map(list, zip(*expanded_transposed)))

coords = []

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if matrix[i][j] == '#':
      coords.append([i, j])

ans = 0

for i in range(0, len(coords) - 1):
  for j in coords[i + 1 :]:
    ans += abs(coords[i][0] - j[0]) + abs(coords[i][1] - j[1])

print(ans)