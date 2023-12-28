with open('input4.txt', 'r') as f:
  lines = f.readlines()

ans = 0

for card in lines:
  card_points = 0

  card = card.strip('\n')
  [game, numbers] = card.split(':')
  [winning_numbers, my_numbers] = numbers.split('|')

  winning_numbers = winning_numbers.strip().split(' ')
  my_numbers = my_numbers.strip().split(' ')
    
  for num in my_numbers:
    if num.isnumeric() and num in winning_numbers:
      if card_points == 0:
        card_points = 1

      else:
        card_points *= 2

  ans += card_points

print(ans)
