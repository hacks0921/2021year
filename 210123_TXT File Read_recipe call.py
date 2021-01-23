recipe = {}
with open('recipe.txt') as f:
    for line in f:
        key, value = line.strip().split(' = ')
        recipe[key] = value
print(recipe.keys())
print(recipe.values())

parameter = recipe.get("parameter")
size = recipe.get("size")
image_h = recipe.get("image_h")
image_w = recipe.get("image_w")

print(recipe)

# parameter = 11
# size = 12
# image_h = 50
# image_w = 50