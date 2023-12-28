def get_last_letters(nodes):
  last_letters = ''

  for i in nodes:
    last_letters += i[-1]

  return last_letters

with open('/Users/mac2/Downloads/input8.txt', 'r') as f:
  lines = f.readlines()

instructions = lines[0].strip('\n')
instructions = instructions.replace('L', '0').replace('R', '1')
inst_len = len(instructions)

nodes = dict()

for i in lines[2:]:
  [node, options] = i.split('=')
  options = options.strip().strip('(').strip(')').split(', ')

  nodes[node.strip()] = options

current_node = []

for i in nodes:
  if i[-1] == 'A':
    current_node.append(i)

current_lasts = get_last_letters(current_node)

current_instruction = 0
steps = 0

while current_lasts != 'ZZZZZZ':
  steps += 1

  new_nodes = []

  for i in current_node:
    new_nodes.append(nodes[i][int(instructions[current_instruction])])

  current_node = new_nodes.copy()
  current_lasts = get_last_letters(current_node)

  current_instruction = (current_instruction + 1) % inst_len

print(steps)
