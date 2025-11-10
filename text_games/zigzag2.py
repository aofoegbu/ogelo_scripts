# Zigzag program

output = "------------"
space = ' '
for count in range(3):
  for i in range(5):
    print(space * i + output)
  for i in range(4,-1,-1):
    print(space * i + output)