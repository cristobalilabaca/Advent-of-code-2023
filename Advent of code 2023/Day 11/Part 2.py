with open('input11.txt', 'r') as f:
  lines = f.readlines()

matrix = []

for i in lines:
  if '#' not in i:
    matrix.append(['i'] * len(i))

  else:
    matrix.append(list(i.strip('\n')))

transposed_matrix = list(map(list, zip(*matrix)))

expanded_transposed = []

for i in transposed_matrix:
  if '#' not in i:
    expanded_transposed.append(['i'] * len(i))

  else:
    expanded_transposed.append(list(i))

matrix = list(map(list, zip(*expanded_transposed)))

coords = []

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if matrix[i][j] == '#':
      coords.append([i, j])

ans = 0

for i in range(0, len(coords) - 1):
  for j in coords[i + 1:]:
    ans += abs(coords[i][0] - j[0]) + abs(coords[i][1] - j[1])

    i_amount = 0

    if coords[i][1] != j[1]:
      row_cero_extrapolation = matrix[0][
        min(coords[i][1], j[1]) : max(coords[i][1], j[1])
      ]

      i_amount += row_cero_extrapolation.count('i')

    if coords[i][0] != j[0]:
      column_cero_extrapolation = expanded_transposed[0][
        min(coords[i][0], j[0]): max(coords[i][0], j[0])
      ]

      i_amount += column_cero_extrapolation.count('i')

    ans += 999999 * i_amount

print(ans)
