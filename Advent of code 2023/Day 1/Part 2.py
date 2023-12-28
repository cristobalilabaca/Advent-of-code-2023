with open("input1.txt", "r") as f:
  lines = f.readlines()

digits = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

sum_res = 0

for line in lines:
  min_index = 10000000
  max_index = -1

  min_value = 0
  max_value = 10

  for i in digits:
    if i in line:
      i_min_index = line.index(i)

      if i_min_index < min_index:
        min_index = i_min_index
        min_value = digits[i]

      i_max_index = line.rindex(i)

      if i_max_index > max_index:
        max_index = i_max_index
        max_value = digits[i]

  sum_res += min_value * 10 + max_value

print(sum_res)
