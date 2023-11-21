import random
roll1 = 0
roll2 = 0

doubles = 0
for i in range(100):
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  if roll1 == roll2:
    doubles += 1

print("Out of 100 you rolled", doubles, "doubles")
