with open('input2.txt', 'r') as f:
  lines = f.readlines()

ans = 0

for line in lines:
  line = line.strip('\n')
  [game, subsets] = line.split(':')
  game_id = game.split(' ')[1]
  subsets = subsets.split(';')
    
  max_red = 0
  max_green = 0
  max_blue = 0

  for subset in subsets:
    subset = subset.split(',')

    for i in subset:
      i = i.strip(' ')
      [amount, color] = i.split(' ')

      if (color == 'red' and int(amount) > max_red):
        max_red = int(amount)

      elif (color == 'green' and int(amount) > max_green):
        max_green = int(amount)

      elif (color == 'blue' and int(amount) > max_blue):
        max_blue = int(amount)
                
  ans += max_red * max_green * max_blue

print(ans)