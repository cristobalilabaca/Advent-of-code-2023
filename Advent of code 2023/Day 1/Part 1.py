with open('input1.txt', 'r') as f:
  lines = f.readlines()

sum_res = 0

for line in lines:
  calib_val = 0

  for i in line:
    if i.isnumeric():
        calib_val += int(i) * 10
        break

  for i in line[::-1]:
    if i.isnumeric():
      calib_val += int(i)
      break

sum_res += calib_val

print(sum_res)
