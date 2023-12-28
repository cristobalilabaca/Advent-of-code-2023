from collections import namedtuple

tile = namedtuple('tile', ['coord', 'symbol', 'prev_coord'])

def find_next_coord(tile):
  match tile.symbol:
    case '-':
      if tile.prev_coord == [tile.coord[0], tile.coord[1] - 1]:
        return [tile.coord[0], tile.coord[1] + 1]

      else:
        return [tile.coord[0], tile.coord[1] - 1]

    case '|':
      if tile.prev_coord == [tile.coord[0] + 1, tile.coord[1]]:
        return [tile.coord[0] - 1, tile.coord[1]]

      else:
        return [tile.coord[0] + 1, tile.coord[1]]

    case 'L':
      if tile.prev_coord == [tile.coord[0], tile.coord[1] + 1]:
        return [tile.coord[0] - 1, tile.coord[1]]

      else:
        return [tile.coord[0], tile.coord[1] + 1]

    case 'J':
      if tile.prev_coord == [tile.coord[0], tile.coord[1] - 1]:
        return [tile.coord[0] - 1, tile.coord[1]]

      else:
        return [tile.coord[0], tile.coord[1] - 1]

    case 'F':
      if tile.prev_coord == [tile.coord[0], tile.coord[1] + 1]:
        return [tile.coord[0] + 1, tile.coord[1]]

      else:
        return [tile.coord[0], tile.coord[1] + 1]

    case '7':
      if tile.prev_coord == [tile.coord[0], tile.coord[1] - 1]:
        return [tile.coord[0] + 1, tile.coord[1]]

      else:
        return [tile.coord[0], tile.coord[1] - 1]

with open('input10.txt', 'r') as f:
  lines = f.readlines()

grid_results = []

grid = []

starting_coordinate = [0,0]

for line in range(len(lines)):
  grid.append(list(lines[line].strip('\n')))
  grid_results.append(['x']* (len(lines[line]) - 1))

  if 'S' in lines[line]:
    starting_coordinate = [line, lines[line].index('S')]
    grid_results[starting_coordinate[0]][starting_coordinate[1]] = 'S'

current_tiles = []

if (
  grid[starting_coordinate[0] + 1][starting_coordinate[1]] == '|'
  or  grid[starting_coordinate[0] + 1][starting_coordinate[1]] == 'J'
  or grid[starting_coordinate[0] + 1][starting_coordinate[1]] == 'L'
):
  current_tiles.append(
    tile(
      [starting_coordinate[0] + 1, starting_coordinate[1]],
      grid[starting_coordinate[0] + 1][starting_coordinate[1]],
      [starting_coordinate[0], starting_coordinate[1]]
    )
  )

if (
  grid[starting_coordinate[0] - 1][starting_coordinate[1]] == '|'
  or  grid[starting_coordinate[0] - 1][starting_coordinate[1]] == '7'
  or grid[starting_coordinate[0] - 1][starting_coordinate[1]] == 'F'
):
  current_tiles.append(
    tile(
      [starting_coordinate[0] - 1, starting_coordinate[1]],
      grid[starting_coordinate[0] - 1][starting_coordinate[1]],
      [starting_coordinate[0], starting_coordinate[1]]
    )
  )

if (
  grid[starting_coordinate[0]][starting_coordinate[1] + 1] == '-'
  or  grid[starting_coordinate[0]][starting_coordinate[1] + 1] == '7'
  or grid[starting_coordinate[0]][starting_coordinate[1] + 1] == 'J'
):
  current_tiles.append(
    tile(
      [starting_coordinate[0], starting_coordinate[1] + 1],
      grid[starting_coordinate[0]][starting_coordinate[1] + 1],
      [starting_coordinate[0], starting_coordinate[1]]
    )
  )

if (
  grid[starting_coordinate[0]][starting_coordinate[1] - 1] == '-'
  or  grid[starting_coordinate[0]][starting_coordinate[1] - 1] == 'L'
  or grid[starting_coordinate[0]][starting_coordinate[1] - 1] == 'F'
):
  current_tiles.append(
    tile(
      [starting_coordinate[0], starting_coordinate[1] - 1],
      grid[starting_coordinate[0]][starting_coordinate[1] - 1],
      [starting_coordinate[0], starting_coordinate[1]]
    )
  )

steps = 1

grid_results[current_tiles[0].coord[0]][current_tiles[0].coord[1]] = current_tiles[0].symbol
grid_results[current_tiles[1].coord[0]][current_tiles[1].coord[1]] = current_tiles[1].symbol

while (
  current_tiles[0].coord != current_tiles[1].coord
  and current_tiles[0].coord != current_tiles[1].prev_coord
):
  tile_one = find_next_coord(current_tiles[0])
  tile_two = find_next_coord(current_tiles[1])

  current_tiles = [
    tile(tile_one, grid[tile_one[0]][tile_one[1]], current_tiles[0].coord),
    tile(tile_two, grid[tile_two[0]][tile_two[1]], current_tiles[1].coord)
  ]

  steps += 1

  grid_results[current_tiles[0].coord[0]][current_tiles[0].coord[1]] = current_tiles[0].symbol
  grid_results[current_tiles[1].coord[0]][current_tiles[1].coord[1]] = current_tiles[1].symbol

print(steps)
