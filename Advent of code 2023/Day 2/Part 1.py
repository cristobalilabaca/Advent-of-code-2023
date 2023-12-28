with open('input2.txt', 'r') as f:
  lines = f.readlines()

ans = 0

for line in lines:
  line = line.strip('\n')
  [game, subsets] = line.split(':')

  game_id = game.split(' ')[1]
  subsets = subsets.split(';')
  possible = True

  for subset in subsets:
    subset = subset.split(',')

    for i in subset:
      i = i.strip(' ')
      [amount, color] = i.split(' ')

      if (color == 'red' and int(amount) > 12) or (color == 'green' and int(amount) > 13) or (color == 'blue' and int(amount) > 14):
        possible = False
        break

  if possible:
    ans += int(game_id)

print(ans)