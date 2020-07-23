pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
ingredient_input = input()
recipe = ""
if ingredient_input in pasta:
    recipe = recipe + "pasta time!\n"
if ingredient_input in apple_pie:
    recipe = recipe + "apple pie time!\n"
if ingredient_input in ratatouille:
    recipe = recipe + "ratatouille time!\n"
if ingredient_input in chocolate_cake:
    recipe = recipe + "chocolate cake time!\n"
if ingredient_input in omelette:
    recipe = recipe + "omelette time!\n"
print(recipe)
