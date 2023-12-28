cards_values = {
    "A": "a",
    "K": "b",
    "Q": "c",
    "J": "d",
    "T": "e",
    "9": "f",
    "8": "g",
    "7": "h",
    "6": "i",
    "5": "j",
    "4": "k",
    "3": "l",
    "2": "m",
}

def card_to_value(card):
  res = ''

  for i in card[:5]:
    res += cards_values[i]

  return res



with open('input7.txt', 'r') as f:
  lines = f.readlines()

hands_classifications = [[], [], [], [], [], [], []]

for i in lines:
  i = i.strip('\n')
  hand = i.split(' ')[0]
  amounts = dict()

  for card in hand:
    if card in amounts:
      amounts[card] += 1

    else:
      amounts[card] = 1
  
  amounts_values = amounts.values()

  if 5 in amounts_values:
    hands_classifications[0].append(i)

  elif 4 in amounts_values:
    hands_classifications[1].append(i)

  elif 3 in amounts_values and 2 in amounts_values:
    hands_classifications[2].append(i)

  elif 3 in amounts_values:
    hands_classifications[3].append(i)

  elif list(amounts_values).count(2) == 2:
    hands_classifications[4].append(i)

  elif 2 in amounts_values:
    hands_classifications[5].append(i)

  else:
    hands_classifications[6].append(i)

for i in range(len(hands_classifications)):
  hands_classifications[i] = sorted(hands_classifications[i], key=card_to_value)

winnings = 0
points = len(lines)

for i in hands_classifications:
  for j in i:
    hand_points = j.split(' ')[1]
    winnings += int(hand_points) * points

    points -= 1

print(winnings)
