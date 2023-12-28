with open('input8.txt', 'r') as f:
  lines = f.readlines()

instructions = lines[0].strip('\n')
instructions = instructions.replace('L', '0').replace('R', '1')

nodes = dict()

for i in lines[2:]:
  [node, options] = i.split('=')
  options = options.strip().strip('(').strip(')').split(', ')

  nodes[node.strip()] = options

current_node = 'AAA'
current_instruction = 0
steps = 0

while current_node != 'ZZZ':
  steps += 1
  current_node = nodes[current_node][int(instructions[current_instruction])]

  current_instruction = (current_instruction + 1) % len(instructions)

print(steps)
