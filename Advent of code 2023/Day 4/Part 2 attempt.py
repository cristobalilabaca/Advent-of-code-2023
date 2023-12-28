with open('input4.txt', 'r') as f:
  lines = f.readlines()

ans = {}

for card in lines:
  card_points = 0

  card = card.strip('\n')
  [game, numbers] = card.split(':')
  game_id = int(game.split(' ')[-1])

  [winning_numbers, my_numbers] = numbers.split('|')
  winning_numbers = [winning_numbers[x: x + 3] for x in range(0, len(winning_numbers) - 1, 3)]
  my_numbers = [my_numbers[x: x + 3] for x in range(0, len(my_numbers), 3)]

  for num in my_numbers:
    if num.strip().isnumeric() and num in winning_numbers:
      card_points += 1
            
  multiplier = 1

  if game_id in ans:
    multiplier = ans[game_id]

  for i in range(0, card_points + 1):
    if game_id + i in ans:
      ans[game_id + i] += multiplier

    else:
      ans[game_id + i] = multiplier

print(sum(ans.values()))
