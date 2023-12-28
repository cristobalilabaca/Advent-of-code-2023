with open('input5.txt', 'r') as f:
  lines = f.read()

lines = lines.split('\n\n')
lines[-1] = lines[-1].strip('\n')

seeds_ranges = lines[0].split(': ')[1].split(' ')
seeds = []

for i in range(0, len(seeds_ranges), 2):
  seeds.append([int(seeds_ranges[i]), int(seeds_ranges[i]) + int(seeds_ranges[i + 1]) - 1])

maps = lines[1:]
maps = [map_info.split('\n')[1:] for map_info in maps]

for i in range(len(maps)):
  for j in range(len(maps[i])):
    maps[i][j] = maps[i][j].split(' ')

seeds_locations = []

current_range = seeds

for i in maps:
  this_ranges = []

  for j in current_range:
    for k in i:
      if int(k[1]) <= j[0] < int(k[1]) + int(k[2]) - 1 and int(k[1]) <= j[1] <= int(k[1]) + int(k[2]) - 1:
        this_ranges.append([j[0] - int(k[1]) + int(k[0]), j[1] - int(k[1]) + int(k[0])])
        j[0] = 0
        j[1] = 0
        break

      elif int(k[1]) <= j[1] <= int(k[1]) + int(k[2]) - 1:
        this_ranges.append([int(k[0]), j[1] - int(k[1]) + int(k[0])])
        j[1] = int(k[1]) - 1

      elif int(k[1]) <= j[0] <= int(k[1]) + int(k[2]) - 1:
        this_ranges.append([j[0] - int(k[1]) + int(k[0]), int(k[0]) + int(k[2]) - 1])
        j[0] = int(k[1]) + int(k[2])

    if j[1] - j[0] > 0:
      this_ranges.append(j)

  current_range = this_ranges

mins = map(lambda x: x[0], current_range)

print(min(mins))
