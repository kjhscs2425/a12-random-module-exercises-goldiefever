import random
def twister_spin():
    colors = ["red", "yellow", "green", "blue"]
    limb = ["arm", "leg"]
    side=["left", "right"]
    print(random.choice(side))
    print(random.choice(limb))
    print(random.choice(colors))
    print("\n")


# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  twister_spin()