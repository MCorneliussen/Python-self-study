################### Scope ####################

enemies = 2

def increase_enemies():
  #global enemies
  #enemies += 1
  print(f"enemies inside function: {enemies}")
  #return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

