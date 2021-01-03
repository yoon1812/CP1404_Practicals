import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 1?
# Ans: random integer
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 5 and the largest was 20

# What did you see on line 2?
# Ans:randomly selected number from range
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 3 and the largest was 9
# Could line 2 have produced a 4?
# No

# What did you see on line 3?
# Ans: random float
# What was the smallest number you could have seen, what was the largest?
# The smallest number was 2.5 and the largest was 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
