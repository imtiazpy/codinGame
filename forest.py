# Lily was crossing a thick forest when she realizes that there is a tiger ahead of her who has seen Lily. Lily quickly takes out a matchbox from her bag and burns a matchstick, because the tiger is afraid of fire. A matchstick takes 5 seconds to burn completely.
# Given that the length of the forest that Lily needs to cross is l meters , and that Lily's speed is s centimeters per second, print the minimum number of matchsticks Lily needs to burn to cross the forest safely.
# Input
# Line 1: An integer l for the length of the forest in meters.
# Line 2: An integer s for Lily's speed in centimeters per second.
# Output
# Line 1: An integer for the least amount of matchsticks Lily needs to burn to safely cross the forest.

import math
i=input
l=int(i())
s=int(i())
print(math.ceil(l/(s/20)))
# print((l//(s//100))//5)