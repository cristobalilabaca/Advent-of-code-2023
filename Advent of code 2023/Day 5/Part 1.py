with open('input5.txt', 'r') as f:
  lines = f.read()

lines = lines.split('\n\n')
lines[-1] = lines[-1].strip('\n')

seeds = lines[0].split(': ')[1].split(' ')
maps = lines[1:]
maps = [map_info.split('\n')[1:] for map_info in maps]

for i in range(len(maps)):
  for j in range(len(maps[i])):
    maps[i][j] = maps[i][j].split(' ')

seeds_locations = []

for i in seeds:
  current_num = int(i)

  for j in maps:
    for k in j:
      if int(k[1]) <= current_num < int(k[1]) + int(k[2]):
        current_num = current_num - int(k[1]) + int(k[0])
        break

  seeds_locations.append(current_num)

print(min(seeds_locations))
